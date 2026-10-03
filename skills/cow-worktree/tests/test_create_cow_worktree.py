#!/usr/bin/env python3
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


HELPER = Path(__file__).parents[1] / "scripts" / "create-cow-worktree"


def run(args, cwd, check=True):
    result = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stderr or result.stdout}")
    return result


def git(cwd, *args, check=True):
    return run(["git", *args], cwd, check=check)


class CowWorktreeSubmoduleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="cow-worktree-test-")
        self.root = Path(self.temp.name)
        self.child = self.root / "child-source"
        self.parent = self.root / "parent"
        self.child.mkdir()
        self.parent.mkdir()
        git(self.child, "init")
        git(self.child, "config", "user.email", "test@example.invalid")
        git(self.child, "config", "user.name", "COW Test")
        (self.child / "child.txt").write_text("pinned child\n")
        git(self.child, "add", "child.txt")
        git(self.child, "commit", "-m", "child")
        self.child_commit = git(self.child, "rev-parse", "HEAD").stdout.strip()

        git(self.parent, "init")
        git(self.parent, "config", "user.email", "test@example.invalid")
        git(self.parent, "config", "user.name", "COW Test")
        (self.parent / "root.txt").write_text("root\n")
        git(self.parent, "add", "root.txt")
        git(self.parent, "commit", "-m", "root")
        git(self.parent, "-c", "protocol.file.allow=always", "submodule", "add", str(self.child), "child")
        git(self.parent, "commit", "-m", "add child")

    def tearDown(self):
        self.temp.cleanup()

    def create(self, branch, destination):
        return run(
            [sys.executable, str(HELPER), "--repo", str(self.parent), "--branch", branch, "--worktree", str(destination)],
            self.root,
            check=False,
        )

    def test_cow_worktree_materializes_pinned_submodule(self):
        target = self.root / "feature"
        result = self.create("feature/submodule", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("mode=cow", result.stdout)
        self.assertEqual(git(target, "status", "--porcelain=v1").stdout, "")
        self.assertEqual(git(target / "child", "rev-parse", "HEAD").stdout.strip(), self.child_commit)
        self.assertTrue((target / "child" / ".git").is_file())
        self.assertEqual((target / "child" / "child.txt").read_text(), "pinned child\n")

    def test_dirty_source_submodule_is_not_used_as_cow_input(self):
        (self.parent / "child" / "child.txt").write_text("private dirty edit\n")
        target = self.root / "clean-feature"
        result = self.create("feature/clean-submodule-input", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / "child" / "child.txt").read_text(), "pinned child\n")
        self.assertEqual((self.parent / "child" / "child.txt").read_text(), "private dirty edit\n")

    def test_missing_pinned_commit_leaves_no_branch_or_worktree(self):
        unavailable = "1" * 40
        git(self.parent, "update-index", "--cacheinfo", f"160000,{unavailable},child")
        git(self.parent, "commit", "-m", "unavailable pin")
        target = self.root / "failed-feature"
        result = self.create("feature/unavailable-pin", target)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Pinned submodule commit is unavailable locally", result.stderr)
        self.assertFalse(target.exists())
        self.assertEqual(git(self.parent, "branch", "--list", "feature/unavailable-pin").stdout, "")
        self.assertNotIn(str(target), git(self.parent, "worktree", "list", "--porcelain").stdout)

    def test_cow_worktree_materializes_nested_pinned_submodules(self):
        grandchild = self.root / "grandchild-source"
        grandchild.mkdir()
        git(grandchild, "init")
        git(grandchild, "config", "user.email", "test@example.invalid")
        git(grandchild, "config", "user.name", "COW Test")
        (grandchild / "nested.txt").write_text("nested pin\n")
        git(grandchild, "add", "nested.txt")
        git(grandchild, "commit", "-m", "nested")
        nested_commit = git(grandchild, "rev-parse", "HEAD").stdout.strip()

        git(self.child, "-c", "protocol.file.allow=always", "submodule", "add", str(grandchild), "nested")
        git(self.child, "commit", "-m", "add nested")
        child_with_nested = git(self.child, "rev-parse", "HEAD").stdout.strip()
        git(self.parent / "child", "-c", "protocol.file.allow=always", "fetch", "origin")
        git(self.parent / "child", "checkout", "--detach", child_with_nested)
        git(self.parent / "child", "-c", "protocol.file.allow=always", "submodule", "update", "--init", "--recursive")
        git(self.parent, "add", "child")
        git(self.parent, "commit", "-m", "pin nested child")

        target = self.root / "nested-feature"
        result = self.create("feature/nested-submodule", target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(git(target, "status", "--porcelain=v1").stdout, "")
        self.assertEqual(git(target / "child", "rev-parse", "HEAD").stdout.strip(), child_with_nested)
        self.assertEqual(git(target / "child" / "nested", "rev-parse", "HEAD").stdout.strip(), nested_commit)
        self.assertEqual((target / "child" / "nested" / "nested.txt").read_text(), "nested pin\n")


if __name__ == "__main__":
    if sys.platform != "darwin":
        raise SystemExit("These tests require macOS cp -c support")
    unittest.main()
