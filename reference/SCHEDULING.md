# Give a useful method a schedule

A skill defines how to do a task. A scheduler decides when and where it runs. Writing a routine file does not register a schedule.

Start with one useful result and prove the method manually. Agree the workspace, sources, input period, executor, model, cadence/timezone, allowed writes, output/reviewer, usage limits, run history and pause control. Use one active scheduler for a job.

Choose execution based on access:

- **Local:** can work with the files/tools available on that computer. The machine and relevant app/session must be available.
- **Hosted:** can keep running without the laptop, but needs its own reachable context, tools and persistence. A local folder is not automatically available there.
- **An ordinary script:** often suits exact transformations, backups and deterministic checks without a model call.

For Codex, check the actual desktop Scheduled surface and workspace access. Local tasks need the computer on and app running; the CLI/IDE extension does not provide the Scheduled management interface. Web tasks use available hosted context rather than directly opening a computer folder. [Official OpenAI guidance](https://learn.chatgpt.com/docs/automations).

For Claude, distinguish a temporary `/loop` in a running Code session from Desktop local scheduled tasks and hosted routines. Verify the actual product, plan, environment and permissions before setup. [Session tasks](https://code.claude.com/docs/en/scheduled-tasks), [Desktop tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks), [Hosted routines](https://code.claude.com/docs/en/routines).

Adapt [the routine example](../routine-example/ROUTINE.md) only after choosing a real job. Start with internal drafts and scoped permissions. Test missing-input behaviour as well as a successful run. Enable only after the user's agreement, read back the registered configuration and verify a scheduled run separately.

Keep evidence where the next run can reach it. Fresh cloud checkouts do not preserve uncommitted local logs. Make late runs and missing/stale data visible. Show the user where to inspect results and pause the job.

References checked 19 October 2026. Actual setup and run verification need the user's environment.
