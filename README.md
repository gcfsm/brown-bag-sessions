# IT Group Hub — Church IT Discipleship & Career Track

## Purpose

A biweekly, workshop-format group for church attendees — students and working
IT professionals alike — to build real IT / software engineering skills, with
Claude Sonnet 5 as an AI-assisted development partner, culminating in
contributing to real church software projects.

## Format

- **Cadence:** Biweekly, alternating short lecture/demo + hands-on lab per topic pairing
- **Group size:** 4–6 people, workshop style (not lecture-hall)
- **Approach:** Theory and manual execution first (no AI shortcuts for core
  mechanics like Git/PRs), AI-assisted workflows introduced explicitly once
  fundamentals are solid
- **Sandbox:** All sessions build against
  [`gcfsm/brown-bag-sandbox`](https://github.com/gcfsm/brown-bag-sandbox) —
  attendees fork it once, in Session 1, and keep building on that same fork
  across every session, so skills (and the project itself) compound over
  time. See `/sandbox` in this repo for details.
- **Gate to real work:** Once attendees can read/write an Epic with Acceptance
  Criteria (Session 19), they're eligible to pair on real church project tickets

## Audience

- **Students** — new to software development
- **Working IT professionals** — experienced but not yet AI-native in their workflow

Both tracks converge in the same room; more experienced attendees informally
mentor students during labs rather than running a separate curriculum.

## Structure

See [`CURRICULUM.md`](./CURRICULUM.md) for the full session-by-session outline.

Each session lives in `/sessions/NN-topic-slug/` and contains:
- `README.md` — session outline, goals, agenda, homework (this is the file
  to fill in with full detail per session)
- Any handouts, cheat sheets, or lab briefs specific to that session

## Status Legend (used in CURRICULUM.md and session READMEs)

- `[ ] Not started` — outline only
- `[~] In progress` — being drafted
- `[x] Ready` — full session content complete, ready to teach

## Repo Structure

```
it-group-hub/
├── README.md                 # this file
├── CURRICULUM.md             # full session-by-session master list
├── sessions/
│   ├── 01-git-basics/
│   ├── 02-cicd-actions/
│   ├── ...
│   └── 20-capstone-real-project/
├── resources/
│   └── cheat-sheets/         # cross-session quick references
└── sandbox/                  # shared practice repo / project used across sessions
```
