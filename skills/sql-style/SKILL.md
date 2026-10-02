---
name: sql-style
description: Write, review, and optimize SQL in Daniel's compact analytical style. Use for SQL queries, Snowflake worksheets, views, and production reporting queries, with stricter contracts for recurring or shared use.
---

# SQL style

- Keep SQL compact enough to read the calculation at a glance. Expand where the logic needs room.
- Use lowercase keywords and functions, snake_case aliases, and four-space indentation. Omit `as` for straightforward column aliases. Preserve quoted identifiers and JSON key casing.
- Put dimensions first, then base metrics, then derived metrics. Keep small related expressions on one line; use leading commas for longer select lists.
- Build CTEs around useful stages: source, aggregate, compare, score. Each stage should explain a calculation or establish a grain. Give them short names that explain their role.
- Reuse metric aliases when the dialect supports it and names resolve unambiguously. In Snowflake, favor `using`, `qualify`, `iff`, `count_if`, and typed JSON paths when they make the query shorter and clearer. Follow the actual engine elsewhere.
- Use brief `--` comments for intent, assumptions, thresholds, or surprising logic. Let straightforward SQL explain itself.

## Short analysis queries

- Default here for one-off questions, exploration, and worksheet checks. Write the smallest complete query that answers the question.
- Use familiar metric shorthand: `sp`, `r`, `p`, `se`, `i`, `rps`, `roi`, `sov`. Keep related calculations together, such as `sum(spend) sp, sum(revenue) r, r-sp p`.
- Use `group by all` and positional ordering when the grain and select list are easy to see. Use `where true` for a growing filter list, with each optional predicate on its own line.
- Use bounded `select *` for inspection and Snowflake `->>` chains for follow-up analysis when useful. Keep each result easy to inspect.

## Production queries

- Use these rules for views, scheduled jobs, application queries, and reports others depend on. Keep the same compact layout.
- Make the row grain, output columns, metric units, and dependencies explicit. Use descriptive output names and named grouping and ordering keys. Keep shorthand inside intermediate calculations when clear.
- Put tunable thresholds and time bounds together. Make date boundaries and timezone assumptions explicit; use ISO dates. Prefer half-open timestamp windows for adjacent periods.
- Check join cardinality before combining metrics. Aggregate each side to the intended grain when needed. Preserve unmatched rows deliberately; check filters on the nullable side of outer joins. Give deduplication and top-row selection a meaningful order and tie policy.
- Define what zero and missing data mean. Use `div0` when a zero denominator should produce zero. Preserve undefined ratios as null when that conveys the result. Calculate aggregate rates from aggregate numerators and denominators when the metric requires weighting.
- Filter source rows early, select needed columns, and remove sorts that do not affect a window, limit, or final result. Prefer predicates that support pruning. Preserve results during optimization and confirm speed claims with a query profile when available.
- Check representative totals, duplicate keys, empty periods, and boundary cases when execution is available. State what remains unverified.
