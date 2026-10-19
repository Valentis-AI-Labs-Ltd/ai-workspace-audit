# Use your context with more than one assistant

The portable part is the saved working knowledge and method. Logins, tools, permissions, settings and session history need separate verification.

Codex loads `AGENTS.md` through its instruction hierarchy; the repository root and working directory matter. Check from the place the user actually opens, especially with independent nested repositories. [OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Claude Code uses `CLAUDE.md` and supports `@path` imports. A short `CLAUDE.md` importing a shared `AGENTS.md` is one option. Merge useful existing guidance; do not replace it with a template. [Claude documentation](https://code.claude.com/docs/en/memory).

Project skill locations include `.agents/skills/<name>/SKILL.md` for Codex and `.claude/skills/<name>/SKILL.md` for Claude Code. Keep one maintained source with tested adapters/links, or deliberate matching copies and an update procedure. Verify real discovery and invocation in each tool. Reading a skill by an explicit path does not prove automatic discovery. [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills).

Test a small handover: save an actual output, sources, decisions, checks and a next step; open a fresh session in the other assistant; continue from those files. Mark anything unavailable or untested. Pause overlapping writers before switching.

Keep default instructions short and link task-specific detail. Choose models by the work and observed results, rather than keeping the largest setting on for every task.

References checked 19 October 2026. Recheck the installed product when applying setup changes.
