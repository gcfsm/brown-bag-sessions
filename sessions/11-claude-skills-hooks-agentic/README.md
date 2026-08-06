# Session: Claude Skills, Hooks, Githooks, Agentic Loops, MCP Servers

**Status:** [ ] Not started

## Goal

Introduce AI-native development workflows — the differentiator session for working IT professionals new to AI-assisted dev — culminating in building a simple custom MCP server.

## Prerequisites

Session 3 (Vibe Coding), comfort with Git

## Topics to Cover (outline — expand with full detail)

- Claude Skills — what they are, how to write one
- Claude Hooks
- Githooks (pre-commit, pre-push) vs. Claude Hooks — how they differ
- Agentic loops — what "agentic" means in practice
- **`git worktree` for parallel agentic work** (introduced conceptually in Session 1; hands-on here) — checking out multiple branches into separate folders at once, running a Claude session per worktree, avoiding constant branch-switching/stashing when juggling multiple AI-assisted changes in parallel
- Building a small repeatable AI-assisted workflow
- **MCP Servers — Creating an Application with an MCP Server**
  - What MCP (Model Context Protocol) is and why it exists — giving Claude tools to call, not just text to read
  - Anatomy of an MCP server: tools, resources, and how Claude discovers/calls them
  - Difference between a Skill (instructions/knowledge) and an MCP server (actual callable actions/integrations)
  - Building a minimal MCP server from scratch (e.g. wrapping a simple internal API or the sandbox app's data)
  - Connecting the MCP server to Claude and testing a real tool call end-to-end
  - Where this fits for church projects — e.g. an MCP server over Ocean SIS data, generalized for teaching purposes
- **Routines — work that runs without you**
  - Completes the arc this session already sets up: a Skill gives Claude
    *knowledge*, an MCP server gives it *tools*, a Routine gives it *a reason
    to start*. Nobody has to be at a keyboard
  - What one is: a saved prompt plus the repositories, cloud environment and
    connectors it's allowed to touch. Runs on Anthropic's infrastructure, so
    it fires with your laptop shut
  - Three ways to start one, and they're combinable on a single routine:
    - **Schedule** — hourly through weekly, or a one-off at a timestamp.
      Minimum interval is one hour
    - **GitHub event** — pull request or release, with filters on author,
      labels, base/head branch, draft and merged state
    - **API** — POST to a per-routine URL with a bearer token, optionally
      carrying run-specific text. This is how a monitoring alert (Session 15)
      or a deploy pipeline (Session 2) starts one
  - Create from `claude.ai/code/routines`, the Desktop app, or `/schedule` in
    the CLI. `/schedule list`, `update`, `run` manage them
  - **The part that needs saying out loud: a routine runs autonomously — no
    permission prompts.** Whatever you gave it, it can use, writes included.
    So the lesson is scoping, not scheduling:
    - Only the repositories it needs
    - Every connector is attached by default — remove the ones it doesn't need
    - The environment's network policy is the wall around it
  - **It acts as you.** Commits, PRs, Slack messages and tickets carry your
    identity. A routine's mistake is your mistake, with your name on it
  - Guardrail worth knowing: Claude pushes to `claude/`-prefixed branches
    freely, and a push anywhere else is rejected if the branch is protected,
    has someone else's open PR, or carries someone else's commits
  - **Where a routine ends and CI begins** — worth drawing the line explicitly
    or people will try to replace one with the other. CI (Session 2) is a
    deterministic gate: same input, same answer, blocks the merge. A routine
    is judgment: it reads, decides, and proposes. Never make a routine the
    thing that has to pass
  - Cost: routines draw down the same subscription usage as any session
    (Session 3's two clocks), plus a daily cap on runs per account
  - Real examples to show: Ocean runs a weekly security scan and a weekly
    triage routine. Both are the "unattended, repeatable, clear outcome"
    shape that routines suit — and neither one is a merge gate
  - Note for the room: routines are in research preview, so specifics move

## Agenda (TBD)

- [ ] Intro / recap of previous session (5-10 min)
- [ ] Theory / demo segment (TBD)
- [ ] Hands-on lab segment (TBD)
- [ ] Wrap-up / homework assignment (5 min)

## Hands-On Lab (TBD)

_Describe the specific exercise attendees will do against the shared sandbox repo._

## Handout / Cheat Sheet (TBD)

_Link or embed a quick-reference handout, similar to Session 1's Quick Reference Card._

## Homework (TBD)

_What attendees should do before the next session._

## Facilitator Note

This session is now dense (Skills + Hooks + Githooks + Agentic Loops + MCP
Server build + Routines) and the split is no longer optional — it's two
1hr parts:
- **Part A:** Claude Skills, Claude Hooks, Githooks (concepts + comparison)
- **Part B:** Agentic loops, building a minimal MCP server, then Routines
  (hands-on build, needs the most lab time of anything in this block)

Routines belong at the very end of Part B and nowhere else. The whole point
lands only after they've built an MCP server: a routine is what happens when
the thing you built starts itself. Teaching it before that makes it sound
like cron with extra steps.

