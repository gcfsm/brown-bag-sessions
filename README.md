# IT Group Hub — Church IT Discipleship & Career Track

## Purpose

A biweekly, workshop-format group for church attendees — students and working
IT professionals alike — to build real IT / software engineering skills, with
Claude Sonnet 5 as an AI-assisted development partner, culminating in
contributing to real church software projects.

## Why Manual First

Before the format and the schedule, the actual pitch for why this hub is
built the way it is:

I learned to drive on a manual — driving school, the exam, the whole
thing. I don't drive manual day to day anymore, and I still remember the
engine dying on me while I was learning. But one thing stuck: you shift
gears when your speed hits a certain range. That's just where the gears
live.

Years later, driving automatic, I noticed something — stepping fully on
the gas to overtake makes the car struggle. What actually works is
releasing the pedal, then reapplying it. Shifts faster, cleaner. And the
moment I noticed that, I recognized it immediately: that's the same thing
I was doing with the clutch and stick, years ago. I would not have known
to even try that if I'd never learned manual. I'd have just kept flooring
it and wondering why the car felt sluggish.

Now I drive an HEV. No handbrake — there's a mechanism that holds the
car automatically at a stop and releases the moment you hit the pedal.
Genuinely amazing tech. And there are cars now with a single pedal for
both accelerating and braking — some Nissan models do this — and I'll be
honest, I still don't know how that one works. I don't think I need to.

**As the tech gets more convenient, you gravitate toward the convenient
version — and that's fine. That's what it's for.** The point isn't that
you must suffer through manual before you're "allowed" to drive
automatic. The point is that the manual knowledge is *why* the automatic
trick made sense to me the moment I saw it, instead of just being a fact
someone told me to memorize.

That's this hub. Sessions 1 and 2 are the manual gearbox — Git and CI/CD,
by hand, no AI shortcuts. Not because automation is bad. Because once
Claude is doing the driving from Session 3 onward, you'll recognize a
bad diff the same way I recognized that throttle trick — instantly, and
for a reason you can actually explain, not just a habit someone told you
to follow. Vibe code your way in with no fundamentals at all, and you're
the driver who only ever knew automatic: fine, right up until the moment
it isn't.

![Manual, then automatic, then HEV auto-hold, then one-pedal — each stage building on the mental model of the one before it](resources/driving-analogy.svg)

## Format

- **Cadence:** Biweekly, alternating short lecture/demo + hands-on lab per topic pairing
- **Group size:** 4–6 people, workshop style (not lecture-hall)
- **Approach:** Theory and manual execution first (no AI shortcuts for core
  mechanics like Git/PRs), AI-assisted workflows introduced explicitly once
  fundamentals are solid — the "manual gearbox first" reasoning above, not
  a rule for its own sake
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
│   ├── cheat-sheets/         # cross-session quick references
│   └── driving-analogy.svg   # illustration for the "Why Manual First" intro story
└── sandbox/                  # shared practice repo / project used across sessions
```
