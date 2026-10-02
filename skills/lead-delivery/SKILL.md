---
name: lead-delivery
description: Coordinate a complete software change from idea through implementation, tests, review, and release readiness in any repository. Use when a user asks DevSquad to lead or ship a feature.
---

# Lead delivery

Act as the delivery lead. Keep the workflow resumable and evidence-based.

1. Inspect the repository deterministically before reasoning deeply: identify the project type, package manager, source/test layout, contribution rules, current branch, clean/dirty state, and available validation commands.
2. If the request is underspecified, write a concise proposal using `templates/spec.md`. Ask for approval before implementation.
3. After approval, create or update the state checkpoint using `templates/state.md`. Record assumptions and decisions in `templates/decisions.md`.
4. Implement the smallest coherent change. Preserve unrelated user work and never reset or overwrite it.
5. Run focused tests first, then the repository's normal lint/typecheck/test/build commands. Capture exact commands and outcomes.
6. Review the diff for correctness, security, compatibility, and missing tests. Fix issues found, then re-run affected checks.
7. Stop and ask only for material ambiguity, destructive/breaking changes, credentials, or final approval to publish/merge/release.

Do not claim a command ran unless its output is available. Do not invent repository-specific commands. Keep updates short; use the checkpoint to carry detail across sessions.
