# Session: Architecture — One Repo or Many, and One Tenant or Many

**Status:** [~] In progress

**Goal:** By the end of this session you can make two architecture calls that
are cheap to get right early and expensive to reverse late: **how the code is
organised** (one repo or many, one build or many) and **how tenants are
isolated** (one church's data kept genuinely separate from another's). Part A
is ready to teach; Part B is still an outline.

**Contents:** [Two Axes](#the-two-axes-nobody-separates) · [Part A — One Repo or Many?](#part-a--one-repo-or-many) · [Why You Start Monorepo](#a1-why-you-start-with-a-monorepo-and-should) · [The Toll](#a2-the-toll-when-the-monorepo-gets-big) · [Lever 1: Modularise Inside](#a3-lever-1--modularise-inside-the-monorepo-workspaces) · [Lever 2: Fragment — Packages](#a4-lever-2--fragment-into-repos-the-packages-solution) · [Lever 2b: Fragment — Submodules](#a5-lever-2b--fragment-into-repos-the-submodule-solution) · [The Decision](#a6-the-decision--which-lever-when) · [Part B — Multi-Tenant](#part-b--multi-tenant-architecture-outline) · [Hands-On Lab](#hands-on-lab) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

## Prerequisites

Sessions 1–2 (packages, Git, CI build times) and Sessions 6–7 (Firebase) for Part B.

---

## The Two Axes Nobody Separates

This session is genuinely advanced, which is exactly why it gets its own
slot — and the first advanced move is refusing to let two different
questions collapse into one word. People say "monolith," "monorepo,"
"modular," "fragmented" as if they're points on a single line. They're not.
There are **two independent axes**, and almost every argument about repo
structure is really two people each talking about a different one:

| Axis | Question | Ends of the range |
|---|---|---|
| **How many repositories** | Where does the code physically live? | **Monorepo** (one repo) ←→ **Polyrepo** (many repos) |
| **How modular the build is** | Can you build/test one piece without the rest? | **Monolithic build** (all or nothing) ←→ **Modular build** (piece by piece) |

**Say this out loud, because the whole of Part A turns on it:** these two
axes are independent. You can have a **modular monorepo** (one repo, but the
build knows its pieces and only rebuilds what changed) and you can have a
**monolithic polyrepo** (five repos that still all have to move together to
ship anything). The pain people blame on "the monorepo" is almost always the
*monolithic build* axis — and you can fix that axis **without** splitting
into many repos at all. Fragmenting into repos is a different, heavier move
that buys a different thing. Keep the two apart and the decision stops being
a religious war and becomes a checklist.

---

# Part A — One Repo or Many?

## A1. Why You Start With a Monorepo — And Should

Start here, and be unembarrassed about it: **for a new project, one repo with
everything in it is the correct default.** Not the beginner default you
graduate out of — the *correct* one, for as long as it's serving you.

What the single repo gives you, all of it for free:

- **One clone, one `npm install`, one thing to run.** A new volunteer is
  productive after two commands, not ten. (This is Session 1's whole
  post-clone flow, once.)
- **One PR changes everything atomically.** Rename a function used in three
  places and the caller and the callee move in the *same commit*, reviewed
  together, verified together by the *same* CI run (Session 2). There is no
  window where the pieces disagree.
- **One version of the truth.** Everyone is on the same commit of everything.
  There is no "which version of the shared code are you on?" because there's
  only one.
- **Refactoring across boundaries is trivial** — because there are no
  boundaries yet to negotiate across.

**Say this out loud:** every one of those bullets is a real cost you'd be
*adding* by splitting up on day one. Splitting a two-app church project into
five repos because "big companies do microservices" is paying the coupling
tax before you've earned any of the benefit. The curriculum's whole
philosophy holds here — a structure should answer a problem you can actually
feel, not one you read about. **Don't pre-fragment.** Start monorepo.

---

## A2. The Toll — When the Monorepo Gets Big

Here's the honest other half, and it's the reason this section exists at all,
because it's a real, felt experience and not a slide: **the monorepo that was
a gift on day one starts charging rent as the project grows.** Three specific
tolls, in the order you feel them:

1. **The build runs longer.** A naïve monorepo rebuilds *everything* on every
   change. Touch one line in the admin panel and CI recompiles the public
   site too, because nothing told it the two are unrelated. Two apps and some
   shared code, and your green check that used to take ninety seconds now
   takes eight minutes.

2. **The tests run longer.** Same mechanism. The whole suite runs on every
   change, because there's no notion of "only the tests that could possibly
   be affected by *this* change." You wait for hundreds of tests to confirm a
   typo fix in a module the change never touched.

3. **You get blocked by code you didn't write.** This is the one that
   actually stings. In a single build with shared dependencies, **a break
   anywhere is a break everywhere.** Someone else's half-finished module
   doesn't compile, so the whole build is red — and *your* perfectly good
   change can't go green through the same CI until *their* mess is fixed
   first. You came to ship a one-line fix and you're now debugging a module
   you've never opened, because the build won't let you past it. Shared
   dependencies make it worse: one person bumps a library version for their
   feature and quietly breaks yours, in the same repo, on the same install.

**Say this out loud:** none of that is the repo being one repo. **All three
are the build being monolithic** — all-or-nothing, no idea what depends on
what. Look back at the two axes: this is the *second* axis biting, and the
first axis (how many repos) has nothing to do with it yet. That distinction
is the whole reason the next section, not the one after it, is the first
thing to reach for.

---

## A3. Lever 1 — Modularise *Inside* the Monorepo (Workspaces)

The instinct when the toll arrives is "split into separate repos." **Resist
it as the first move.** The first, cheapest, least regrettable lever keeps
the single repo and fixes the *build* axis instead: give the monorepo
internal structure and a build tool that understands it.

**Workspaces** — a first-class feature of npm, pnpm, and yarn — let one repo
hold several packages side by side:

```
church-hub/                 # one repo, one git history, one clone
├── package.json            # workspaces: ["apps/*", "packages/*"]
├── apps/
│   ├── admin/              # the volunteer dashboard  (its own package.json)
│   └── site/               # the public site          (its own package.json)
└── packages/
    └── shared/             # code both apps use        (its own package.json)
```

`apps/admin` can now depend on `packages/shared` by name, and the workspace
tooling symlinks it locally — **no publishing, no version numbers, no second
repo.** You've drawn the module boundaries the naïve monorepo didn't have,
and you've drawn them for free.

The payoff comes when you add a build system that reads those boundaries —
**Turborepo** or **Nx** are the two common ones — and computes the
**affected graph**: given what changed, which packages could *possibly* be
impacted?

| Symptom from A2 | What the affected graph does about it |
|---|---|
| Build rebuilds everything | Rebuilds **only** the changed package and whatever depends on it. Touch `admin`, `site` is skipped. |
| Tests run for the whole repo | Runs **only** the tests reachable from the change. A `shared` change runs both apps' tests; an `admin`-only change runs only `admin`'s. |
| Second run is as slow as the first | **Caches** each task's result keyed by its inputs — unchanged package, instant cache hit, zero rebuild. This is Session 2's `cache: 'npm'` idea, generalised from installs to every build and test task. |

**Say this out loud:** you just fixed the build and test tolls, and you cut
straight into the "blocked by someone else's break" toll too — a red `admin`
no longer stops a `site`-only PR from going green, because the graph knows
they don't touch. **And you did it with the same one repo, one clone, one
atomic PR you started with in A1.** You kept every benefit and paid down the
biggest cost. For most church-scale projects, *this is where the story ends*
— you never need the next two sections in production, only in your head.

**The honest caveat — this axis isn't free either.** You now own a build
config (`turbo.json` / Nx's project graph) and the discipline of declaring
each package's inputs and outputs correctly. Get the input declarations wrong
and the cache serves you a stale result — a green check that verified an old
version of the code, which is Session 2's "a check is only as real as the
thing it runs" failure wearing a new hat. It's a real cost. It's just a much
smaller one than the next two sections.

---

## A4. Lever 2 — Fragment Into Repos: The Packages Solution

Sometimes one repo genuinely isn't the answer — and the tell is **not** build
time (A3 fixed that). The tell is **people and cadence**:

- A different team should own a piece, with their **own permissions**, their
  own reviewers, their own merge rights — without seeing or touching the
  rest.
- A piece needs its **own release schedule** — the shared component library
  ships on Tuesdays and everything else consumes whatever's stable, rather
  than everyone always being on `main` of everything.
- A piece is **shared across projects that aren't in this repo at all** — the
  same auth helpers used by three separate church apps that will never live
  together.

When that's the real need, you fragment — and the cleaner of the two ways to
do it is **published packages.** The shared code becomes its own repo, with
its own CI, and it **publishes versioned releases** to a registry (npm, or
**GitHub Packages** for private ones). The apps that use it list it in
`package.json` like any other dependency — because now it *is* one:

```jsonc
// apps/admin/package.json, in a separate repo from @church/shared
"dependencies": {
  "@church/shared": "^2.1.0"     // a real version, from a registry
}
```

This is the same npm mechanism from Session 1's §1.5 — you're just on the
*publishing* side of it now instead of only the consuming side.

**What you buy:** genuine independence. `@church/shared` has its own history,
its own permissions, its own release cadence, its own green check. An app
pins `^2.1.0` and upgrades **deliberately**, when it chooses, rather than
being dragged along by every commit to `main`.

**What it costs — and this is the part people undersell:**

- **The atomic PR is gone.** A change that spans the shared package *and* an
  app is now **two PRs in two repos**, in order: land and publish
  `@church/shared@2.2.0` first, *then* bump the app to depend on it. You
  cannot review or verify the whole change as one unit anymore — the thing
  the monorepo gave you for free in A1 is exactly the thing you just sold.
- **Version skew is now yours to manage.** App A is on `shared@2.1`, App B is
  still on `2.0`, and a bug report means first asking "which version were you
  running?" — a question that *could not exist* in the monorepo.
- **Release overhead is now a standing job.** Versioning, changelogs,
  publishing, and deciding what's a breaking change (semver) become recurring
  work. Tools like **Changesets** exist specifically because this got painful
  enough to need tooling.

**Say this out loud:** notice what you traded. The monorepo's cost was build
time and coupling, which A3 already fixed. Fragmenting into published
packages buys *ownership and cadence* and pays for it in *coordination* —
a completely different currency. If you don't need separate ownership or
cadence, you're paying that bill for nothing.

---

## A5. Lever 2b — Fragment Into Repos: The Submodule Solution

There's a second way to stitch separate repos together, and you'll meet it in
real church and open-source projects, so it's worth knowing honestly rather
than discovering the hard way: **git submodules.**

A submodule is one repo living *inside* another, **pinned to a specific
commit.** The parent repo doesn't copy the child's code into its own history —
it stores a pointer (a "gitlink") that says "at this path, use *exactly*
commit `a1b2c3d` of that other repo," plus a `.gitmodules` file listing where
each one comes from:

```bash
git submodule add https://github.com/gcfsm/shared.git packages/shared
# parent now records: packages/shared -> commit a1b2c3d of shared.git
```

**When it fits:** you want the separate-repo split (own history, own
permissions) but you want the parent to pin an **exact commit** rather than a
published version number — common for vendored dependencies, shared config,
or a design system consumed by several apps where you don't want the overhead
of publishing to a registry at all.

**Now the honest part, because submodules have a real reputation and it's
earned.** These are the specific ways they bite, and every one of them has
tripped up experienced people:

- **Clone looks empty.** A plain `git clone` of the parent leaves every
  submodule folder *empty* — the pointer came down, the code didn't. New
  contributors hit this on day one and think the repo is broken. The fix is a
  flag nobody remembers the first time:
  ```bash
  git clone --recursive <url>              # clone + fetch all submodules
  git submodule update --init --recursive  # the "oh right" command, after a plain clone
  ```
- **You commit a pointer to a commit nobody else has.** The classic footgun:
  you make a change *inside* the submodule, commit it there, then commit the
  updated pointer in the parent — but **forget to push the submodule.** Now
  the parent points at a commit that exists only on your laptop. Everyone
  else's `submodule update` fails, and it looks like *their* problem. The
  ordering rule is unforgiving: **push the submodule first, then the parent.**
- **Detached HEAD, by default.** `submodule update` checks the child out at a
  bare commit, not on a branch. Edit there without first checking out a
  branch and it's easy to commit into the void. Everyone learns "always
  `git checkout main` inside the submodule before touching it" — after losing
  work once.
- **Updating the pin is a manual, explicit commit** in the parent, every
  time. The parent does **not** track the submodule's `main` automatically —
  it stays frozen on whatever commit you last pinned until a human bumps it.
  That's the feature (reproducibility) and the chore (it's on you), at once.

**An alternative worth naming: `git subtree`.** It solves the same
"one repo inside another" need by actually *copying* the child's code and
history into the parent, so a normal clone just works and there are no
pointers to forget. The trade is a heavier parent history and clunkier
pulling of upstream changes. Many teams that got burned by submodules move to
subtree, or drop back to the published-package approach in A4. **Reach for
submodules deliberately, knowing the tax — not because a tutorial reached for
them first.**

---

## A6. The Decision — Which Lever, When

Put it on one ladder. Climb it **only as far as a felt problem pushes you** —
each rung adds capability and adds cost, and stopping early is a valid, often
correct, answer:

| Rung | You have | Reach for it when | It costs you |
|---|---|---|---|
| **0. Plain monorepo** | One repo, one build | Always — this is the start line | Build/test time and coupling, *once it's big* |
| **1. Modular monorepo** (workspaces + affected-graph build) | One repo, module-aware build/test/cache | The build/test toll is real (A2) — this fixes it | A build config and honest input declarations |
| **2. Polyrepo, published packages** | Many repos, versioned releases | You need separate **ownership** or **release cadence** | Atomic PRs, version-skew management, release overhead |
| **2b. Polyrepo, submodules** | Many repos, pinned by commit | Same as 2, but you want exact-commit pinning over versions | All of rung 2's costs **plus** submodule fiddliness |

**The one rule that prevents most regret:** the build/test toll from A2 is a
**rung 1** problem — solve it at rung 1. Do **not** climb to rung 2 to fix a
slow build, because rung 2 doesn't fix slow builds (a five-repo project still
builds slowly if each build is monolithic) and it hands you coordination
overhead on top. **Climb to rung 2 only for the people-and-cadence reasons in
A4 — separate ownership, separate release schedule, sharing across projects —
never for build speed.** Getting those two motivations confused is the single
most common way small teams end up with submodule pain they never needed.

**Church-scale recommendation, said plainly:** start and very likely *stay*
at **rung 0 or 1.** A two- or three-app church project with one small team has
the build problem (fix it at rung 1 the day it's annoying) and almost never
has the ownership-and-cadence problem (rung 2). If you find yourself reaching
for submodules on a church project, stop and ask whether a workspace would
have done it — the answer is usually yes, at a fraction of the cost.

**Forward and backward links:**
- **Session 1 (§1.5)** taught npm from the *consuming* side; A4 is the same
  mechanism from the *publishing* side.
- **Session 2** taught why CI build minutes cost and why caching matters — A3
  is that idea generalised from installs to every build and test task.
- **Session 16 (Cost Awareness)** comes back to this: a monolithic build
  doesn't just cost wall-clock time, it burns real CI minutes on every push;
  the affected graph is a cost lever, not only a speed one.

---

# Part B — Multi-Tenant Architecture (outline)

**Status:** [ ] Not started — outline only

The second architecture axis: once the code is organised, how do you keep one
church's data genuinely isolated from another's in the same system?

## Topics to Cover (outline — expand with full detail)

- What multi-tenancy means and why it's hard
- Tenant resolution strategies
- Data isolation patterns in Firestore
- Common pitfalls (cross-tenant data leaks)
- Real example walkthrough (Ocean SIS architecture, generalized)

---

## Hands-On Lab

### Part A — Call the rung, in pairs (15 min)

For each scenario, name the rung from A6 (0 / 1 / 2 / 2b) you'd stop at, and
say in one sentence what decided it. Watch for the trap: a *build-speed*
reason never justifies rung 2.

1. A single church app, one small team, CI has crept to seven minutes because
   every push rebuilds and re-tests the whole thing.
2. A public site and an internal admin dashboard that share a component
   library, one team, and touching the library keeps rebuilding both apps.
3. A shared auth/permissions library that three *separate* church apps —
   different teams, different repos, different release schedules — all depend
   on.
4. The scenario in 3, but the lead insists each app pin an exact commit of the
   library, not a version range.

Scenarios 1 and 2 are rung-1 problems in disguise — the honest answer is
"modularise the monorepo," not "split it up." Only 3 introduces a real
ownership/cadence reason to fragment; 4 is the one place submodules earn their
keep over published packages.

### Part B — TBD

_Multi-tenant lab to be designed once Part B is written out._

---

## Quick Reference Card (keep this open while working)

```
TWO AXES — KEEP THEM APART
  how many repos:   monorepo  <----->  polyrepo
  how modular build: monolithic <---> modular (piece-by-piece)
  the "monorepo is slow" pain is the BUILD axis, not the repo count.
  you can fix it WITHOUT splitting into many repos.

THE LADDER — climb only as far as a felt problem pushes you
  0. plain monorepo         start here. always.
  1. modular monorepo       workspaces + Turborepo/Nx affected graph
       -> fixes: long builds, long tests, blocked-by-others' breaks
       -> costs: a build config + honest input declarations
  2. polyrepo + packages    publish @scope/pkg, apps pin ^versions
       -> buys: separate OWNERSHIP + release CADENCE
       -> costs: no atomic PR, version skew, release overhead
  2b. polyrepo + submodules parent pins an exact COMMIT of a child repo
       -> buys: exact-commit pinning instead of versions
       -> costs: everything in rung 2, PLUS submodule fiddliness

THE ONE RULE
  slow build  = rung 1 problem. fix it at rung 1.
  separate ownership / cadence = the ONLY reason to climb to rung 2.
  never fragment repos to make a build faster — it won't, and it's costlier.

SUBMODULE SURVIVAL (if you must)
  git clone --recursive <url>               # or empty folders on plain clone
  git submodule update --init --recursive   # the "oh right" fix after a plain clone
  push the SUBMODULE first, then the parent  # or you pin a commit nobody has
  git checkout main INSIDE the submodule     # before editing — avoids detached HEAD
  alternative: git subtree (copies code in, no pointers) — clunkier history

CHURCH-SCALE DEFAULT
  start and probably stay at rung 0 or 1.
  reaching for submodules on a church project? a workspace almost always
  does it for a fraction of the cost.
```

---

## Homework Before Next Session

- [ ] Open a project you use — idmc-gcfsm, a teammate's, or an open-source
      one — and place it on the ladder: is it a plain monorepo, a modular one
      (look for a `workspaces` field, a `turbo.json`, or an `nx.json`), or
      split across repos (look for `.gitmodules`, or `@scope/`-named
      dependencies that are really your own code)?
- [ ] If you find a monorepo whose CI rebuilds everything on every push, write
      the one-paragraph case for adding workspaces + an affected-graph build —
      which rung it's on, which rung it should be on, and the one sentence of
      why. This is a real, mergeable improvement, not a hypothetical.
- [ ] If you find a submodule in the wild, clone it *wrong* on purpose (plain
      `git clone`, no `--recursive`), watch the empty folder appear, then fix
      it with `git submodule update --init --recursive`. Feeling the failure
      once is worth more than reading the flag ten times.
