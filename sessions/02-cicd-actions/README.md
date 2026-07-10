# IT Group Hub — Session 2: CI/CD & GitHub Actions

**Status:** [x] Ready

**Goal:** By the end of this session, you can read and write a GitHub Actions workflow, understand why a "passing check" gates a merge, set up branch protection that requires it, and read a failed Actions run well enough to fix it — all on the free tier.

**Contents:** [Why CI/CD Exists](#why-cicd-exists--integration-hell) · [GitHub Actions Basics](#1-github-actions-basics) · [Your First Workflow](#2-your-first-workflow-lintest) · [Free-Tier Limits](#3-free-tier-limits--what-they-mean-in-practice) · [Branch Protection](#4-branch-protection--making-checks-mandatory) · [Reading a Failed Run](#5-reading-a-failed-actions-run) · [Dependabot](#6-dependabot--automatic-dependency-prs) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

---

## Why CI/CD Exists — Integration Hell

Session 1 ended on a claim worth re-stating plainly: **Git made branching and
merging cheap.** Anyone can branch off `main`, work in isolation, and merge
back whenever they want, for free, in seconds.

That's necessary — but on its own, it's not sufficient. Here's the gap:

> Ten people each branch off `main` on Monday. Each of them writes code that
> works fine, alone, on their own branch, all week. Friday afternoon,
> everyone merges into `main` at once.

What happens? Nobody knows — until it's tried. Maybe two branches both
renamed the same function differently. Maybe one branch's change to a
shared config quietly broke another branch's feature. Maybe it all works.
The only way to find out, in a world with cheap branching but no
automated verification, is to merge everything and see what catches fire.
Teams that worked this way had a name for Friday afternoon: **integration
hell** — the point where weeks of isolated, individually-fine work collide
all at once, and nobody can tell which of ten simultaneous changes broke
the build.

**Continuous Integration (CI)**, a term coined in the Extreme Programming
movement of the late 1990s, is the direct fix: merge *early and often*
(ideally the same day work starts), and **verify every single merge
automatically** — build it, lint it, test it — so a break is caught in
minutes, on the one small change that caused it, instead of months later,
buried in ten weeks of everyone else's work.

**This is the missing half of Session 1.** Cheap merging (Git) plus
automatic verification on every merge (CI) is what actually makes
"branch → PR → merge, all day, every day" safe at team scale. Git alone
gives you the *ability* to integrate constantly; CI is what makes doing so
*not reckless*.

**Continuous Delivery / Deployment (CD)** is the natural next step once you
trust that: if `main` always passes its checks, `main` is always in a
shippable state — so shipping can itself become automatic (or one click)
instead of its own separate, dreaded event. We'll only touch the edge of
CD today (Session 7 covers actual deploys); the focus here is the CI half —
the automated gate that makes every merge trustworthy in the first place.

**Where this leaves the vibe/agentic thread from Session 1:** if Claude can
propose a change and you can merge it in minutes, CI is what stops "fast"
from becoming "fast and broken." A lint/test workflow doesn't care whether
a human or an AI wrote the diff — it checks the *result*, every time,
without getting tired or skipping a step because the code "looked fine."

---

## 1. GitHub Actions Basics

GitHub Actions is GitHub's built-in CI/CD system: you commit a workflow
file to your repo, GitHub runs it on hosted machines ("runners") in
response to events like a push or a PR, and reports pass/fail back on the
commit and the PR itself.

**Anatomy of a workflow file** — lives at `.github/workflows/<name>.yml`:

```yaml
name: CI                          # shows up in the Actions tab

on:                                # what triggers this workflow
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:                              # one or more jobs, run in parallel by default
  lint-and-test:
    runs-on: ubuntu-latest         # the hosted runner image

    steps:                         # a job is a sequence of steps, run in order
      - uses: actions/checkout@v4  # step 1: get the code onto the runner
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install
      - run: npm run lint
      - run: npm test
```

**The vocabulary that matters:**

| Term | What it means |
|---|---|
| **Workflow** | The whole `.yml` file — one automated process |
| **Trigger** (`on:`) | The event that starts the workflow — `push`, `pull_request`, on a schedule, or manually |
| **Job** | A group of steps that run together on one runner. Multiple jobs run in parallel unless you say otherwise |
| **Step** | One command or one reusable "action" (`uses:`) inside a job, run in order |
| **Action** | A packaged, reusable step someone else wrote (`actions/checkout@v4` is GitHub's own) — same idea as an npm package, but for CI steps |
| **Runner** | The actual (temporary, disposable) virtual machine your job executes on |

**Where to see it run:** the **Actions** tab on the repo. Every push and
every PR gets its own run, with each job and step's live output —
this is also where you'll go to read a failure (Section 5).

---

## 2. Your First Workflow: Lint/Test

The workflow above already *is* a real, working lint/test CI setup — this
section is about actually landing it.

```bash
mkdir -p .github/workflows
```

Then create `.github/workflows/ci.yml` with the content from Section 1.
Commit it on a branch, same as any other change:

```bash
git checkout -b add-ci-workflow
git add .github/workflows/ci.yml
git commit -m "Add CI workflow: lint + test on push and PR"
git push -u origin add-ci-workflow
```

Open a PR (Session 1, Section 5) — and this time, watch what happens on the
PR page itself: a new **"Checks"** section appears, showing `lint-and-test`
running live. When it finishes, you get a green check or a red X directly
on the PR, before anyone even reviews the diff.

**This is the payoff:** a human reviewer no longer has to manually run
`npm test` locally to find out if a PR is broken — the PR tells you before
a human even opens it.

---

## 3. Free-Tier Limits — What They Mean in Practice

GitHub Actions is free within limits — worth knowing so a workflow doesn't
quietly stop running mid-project:

| | Public repos | Private repos (Free plan) |
|---|---|---|
| Actions minutes | **Unlimited** | 2,000 minutes/month |
| Storage (artifacts/caches) | Unlimited | 500 MB |
| Concurrent jobs | Up to 20 | Up to 20 (5 for macOS) |

**Practical notes:**
- Minutes are billed per job, and **Linux runners are cheapest** (macOS
  runners cost 10x the minutes, Windows 2x) — default to `ubuntu-latest`
  unless you specifically need another OS.
- A simple lint/test job usually takes 1–3 minutes. At 2,000 free
  minutes/month, that's several hundred CI runs before you'd need to think
  about cost — plenty for a small church project, but worth knowing the
  ceiling exists (Session 16 — Cost Awareness — comes back to this).
- Church/sandbox projects should default to **public repos** where
  possible, specifically to get unlimited Actions minutes.

---

## 4. Branch Protection — Making Checks Mandatory

Session 1 flagged this: on most real projects, `main` rejects direct
pushes and requires a reviewed PR. **A CI check existing doesn't enforce
anything by itself** — you have to explicitly tell GitHub "don't allow a
merge unless this check passes." That's branch protection.

### Steps
1. Repo → **Settings → Branches**
2. **Add branch protection rule** (or **Add rule**)
3. Branch name pattern: `main`
4. Turn on:
   - **Require a pull request before merging** — no direct pushes to `main`, ever
   - **Require approvals** — at least 1 reviewer, even on a small team
   - **Require status checks to pass before merging** — then search for and select your `lint-and-test` job (only appears in this list *after* the workflow has run at least once)
   - **Require branches to be up to date before merging** — forces you to merge the latest `main` in before merging out, catching integration conflicts before they land (this is the "merge often" half of Section "Why CI/CD Exists" enforced automatically)
5. Save

**What this actually buys you:** the PR **Merge** button itself goes gray
and won't click until the check passes and a reviewer approves. It's no
longer a matter of discipline or remembering — GitHub mechanically refuses
the merge. This is the concrete, hands-on answer to the Session 1 question
"how is a PR ever more than a suggestion?"

---

## 5. Reading a Failed Actions Run

Everyone hits a red X eventually. The workflow, not the panic:

1. On the PR (or the **Actions** tab), click the failed check
2. Click into the failing **job**, then the failing **step** — GitHub
   expands the exact command's output, same as running it in a terminal
3. Read from the **bottom up** — the last few lines are almost always the
   actual error; everything above is setup noise
4. Reproduce **locally** before pushing a fix:
   ```bash
   npm install
   npm run lint    # or whatever step failed
   npm test
   ```
   Fixing blind by pushing again and waiting on CI wastes the very minutes
   Section 3 just covered — confirm the fix locally first
5. Commit the fix, push — the same PR re-runs the check automatically,
   no need to open a new one

**Common first-timer failures, roughly in order of frequency:**
- Node version mismatch (local Node version differs from `node-version:`
  in the workflow — check `.nvmrc` / `engines` per Session 1)
- A file that works locally but was never `git add`-ed / committed
- An environment variable or secret the runner doesn't have (Session 7
  covers secrets properly)
- A flaky/slow test that only fails under CI's constrained resources

---

## 6. Dependabot — Automatic Dependency PRs

Dependabot is a free, built-in GitHub bot that watches `package.json` and
opens a PR automatically whenever a dependency has a newer version — most
importantly, when a version fixes a known security vulnerability.

**Turning it on** — `.github/dependabot.yml`:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
```

**Reading a Dependabot PR:**
- Title tells you the package and version jump: `Bump express from 4.18.1 to 4.18.2`
- The PR description links the changelog/release notes — skim for
  "breaking" or "security"
- **It runs through your CI like any other PR** — this is the entire
  point of Sections 2–4 existing before this one: a version bump either
  passes your lint/test check or it doesn't, automatically

**Security alerts vs. version bumps — different urgency:**

| | Security alert (Dependabot Security) | Routine version bump |
|---|---|---|
| Why it opened | A known CVE in a dependency you use | A newer version just exists |
| Urgency | Review and merge promptly | Merge when convenient, or batch several |
| What to check | Does the CVE actually affect how you use the package? | Does CI still pass? Any breaking changes in the changelog? |

**Safe default:** if CI passes and the changelog shows no breaking
changes, merge it — that's low-risk, automated maintenance. If CI fails,
or the changelog mentions a breaking change, treat it like any other PR
that needs a real look before merging.

---

## Quick Reference Card (keep this open while working)

```
# workflow file lives here
.github/workflows/ci.yml

# minimal lint/test workflow
name: CI
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }
jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install
      - run: npm run lint
      - run: npm test

# reproduce a CI failure locally before re-pushing
npm install
npm run lint
npm test

# branch protection, once a check has run at least once:
# Settings -> Branches -> Add rule -> main
#   [x] Require a pull request before merging
#   [x] Require approvals
#   [x] Require status checks to pass before merging -> select the job
#   [x] Require branches to be up to date before merging

# dependabot.yml — weekly npm dependency PRs
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule: { interval: "weekly" }
```

---

## Homework Before Next Session

- [ ] Add a `.github/workflows/ci.yml` lint/test workflow to your fork of the sandbox repo
- [ ] Open a PR and watch the check run live on it
- [ ] Turn on branch protection on your fork's `main`: require the PR, require the check, require it to be up to date
- [ ] Deliberately break a test or lint rule on a branch, push it, and read the failed run before fixing it
- [ ] Add `.github/dependabot.yml` and, if a PR shows up before next session, read (don't necessarily merge) it
