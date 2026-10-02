---
name: review
description: Review an implementation or diff for correctness, regressions, security, maintainability, compatibility, and test coverage before merge.
---

# Review

Read the diff and surrounding code. Prioritize concrete defects over style. Check boundary cases, error handling, authorization and secret exposure, data migrations, public API compatibility, and whether tests prove the requested behavior. Report findings by severity with file and line references. If no findings remain, say what was checked and identify residual risk.
