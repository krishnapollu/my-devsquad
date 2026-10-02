# DevSquad

DevSquad is a skills-first AI software engineering team for Codex and VS Code workflows. It works with any repository and is zero-server and zero-cost by default: the package contains reusable instructions, templates, and a dependency-free validator; it does not require an API server, database, hosted state, or notification service.

## Workflow

Ask DevSquad to brainstorm or specify a feature. It inspects the repository, drafts a proposal, and waits for approval. After approval, the lead coordinates implementation, focused tests, repository-standard checks, review/fixes, and PR or release readiness. It pauses only for material ambiguity, breaking or destructive changes, credentials, or final publish/merge/release approval.

State is intentionally compact and resumable. Store the active checkpoint under `devsquad/state.md` in the target repository and decisions under `devsquad/decisions.md` when the repository wants persisted project state. The packaged templates are starting points.

## Install and use

Install the plugin from the Codex/ChatGPT plugin directory or load this repository as a local plugin during development. The portable root `plugin.json` is the current manifest; `.codex-plugin/plugin.json` remains as a Codex compatibility fallback. In VS Code, use the same skill files with an agent/plugin host that supports the OpenAI plugin conventions.

Example prompts:

* “DevSquad, inspect this repo and draft a spec for adding CSV export. Do not edit files.”
* “The spec is approved. Implement it, run focused and standard checks, and stop before publishing.”
* “Review the current diff for correctness and release risks. Fix only confirmed issues.”
* “Resume from the DevSquad checkpoint and report the next three actions.”

## Safety and git

DevSquad preserves unrelated user changes and does not use destructive history operations. It must not force-push, rewrite history, delete branches, publish packages, or release production artifacts without explicit approval. Credentials are never requested in chat when a safer user-operated login flow is available.

## Validation

Run `python3 scripts/validate.py` for structural validation and `python3 -m pytest -q` when pytest is available. The validator has no third-party dependencies.

For a target repository, the local helper provides lightweight checkpoints:

```bash
python3 devsquad.py init
python3 devsquad.py status
python3 devsquad.py inspect
python3 devsquad.py validate
```

The repository also includes `AGENTS.md`, Copilot repository instructions, and visible Lead/SDET/Reviewer agent definitions. These are adapters around the same canonical skills, so behavior stays consistent across hosts.

For SDET work, use `templates/test-plan.md` to make risk coverage explicit. Before a PR or release, use `templates/release-checklist.md` so readiness is evidence-based rather than inferred from a green happy-path test.

## Distribution

For personal use, load the folder as a local plugin. For wider distribution, package the root manifest and `skills/` directory, review the official plugin submission requirements, and publish through the supported directory flow. Optional GitHub, Slack, email, or calendar notifications require an explicitly installed and authorized connector; without one, DevSquad produces copy-ready summaries and links rather than pretending to send notifications.

The package follows the official OpenAI plugin model: skills provide workflow instructions and resources; an MCP server is optional and intentionally omitted here. See the [OpenAI plugin skills documentation](https://developers.openai.com/plugins/concepts/skills) and [plugin packaging documentation](https://developers.openai.com/plugins/build/plugins).
