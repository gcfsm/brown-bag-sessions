# IT Group Hub — Session 2: CI/CD & GitHub Actions

**Status:** [x] Ready

**Goal:** By the end of this session, you can read and write a GitHub Actions workflow, understand why a "passing check" gates a merge, set up branch protection that requires it, read a failed Actions run well enough to fix it, and have actually watched a merge deploy itself — all on the free tier, capped off by watching a resolved conflict trigger both the check and the deploy at once.

**Contents:** [Why CI/CD Exists](#why-cicd-exists--integration-hell) · [GitHub Actions Basics](#1-github-actions-basics) · [Your First Workflow](#2-your-first-workflow-lintest) · [Free-Tier Limits](#3-free-tier-limits--what-they-mean-in-practice) · [Branch Protection](#4-branch-protection--making-checks-mandatory) · [Reading a Failed Run](#5-reading-a-failed-actions-run) · [Dependabot](#6-dependabot--automatic-dependency-prs) · [Your First Deploy](#7-your-first-deploy--experiencing-cd) · [Full Loop](#8-full-loop--replay-the-conflict-now-watch-everything-react) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

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
instead of its own separate, dreaded event. Today's focus is the CI half —
the automated gate that makes every merge trustworthy in the first place —
but you don't just hear about CD, you get two doses of it: the facilitator
walks through a **real production pipeline** (with environments, secrets,
the actual complexity — Session 7 territory), and then you build a small,
free, secret-free version yourself in Section 7 below, so "merge triggers
an automatic deploy" is something you've actually watched happen to your
own code, not just a slide.

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

**Where actions come from:** `actions/checkout` and `actions/setup-node`
aren't special-cased — they're two of thousands of published actions on the
[GitHub Actions Marketplace](https://github.com/marketplace?type=actions),
same idea as npm packages but for CI steps. Need to deploy to Firebase,
post to Slack, or run a Lighthouse audit? There's very likely already a
marketplace action for it before you'd write one from scratch.

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

**A visible payoff:** once the workflow has run at least once on `main`,
drop a status badge into your README so the result is visible without
opening the Actions tab:

```markdown
![CI](https://github.com/<owner>/<repo>/actions/workflows/ci.yml/badge.svg)
```

Green means the last run on the default branch passed; red means it
didn't. Small, but it's the first thing a visitor — or a future you —
sees.

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

**Cutting minutes further — cache dependencies:** re-downloading every
package on every single run is the single biggest waster of minutes on a
small project. One extra line fixes it:

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'    # caches node_modules, keyed off package-lock.json
```

This alone can take a ~2-minute install down to a few seconds on a cache
hit — worth adding to the Section 1 workflow once it's running, well
before minutes become a real constraint.

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

## 7. Your First Deploy — Experiencing CD

Everything above is CI: verifying a merge. This section is CD: a merge
**shipping itself**, automatically, with no click required. The
facilitator just walked you through what that looks like in a real
production app — environments, secrets, the genuine complexity Session 7
covers properly. This is the scaled-down version you build yourself,
right now, for free, with nothing to configure but a workflow file.

**Why GitHub Pages for this, not Firebase:** Firebase deploy needs a
service account secret, project setup, sometimes a custom domain — real
infrastructure, correctly deferred to Session 7. GitHub Pages needs
neither an account nor a secret — it deploys straight from the repo you
already have, which makes it the right size for "experience the mechanism
today," not "learn production deployment today."

### Steps

1. Repo → **Settings → Pages** → under **Build and deployment**, set
   **Source** to **GitHub Actions**
2. Add `.github/workflows/deploy.yml`:
   ```yaml
   name: Deploy

   on:
     push:
       branches: [main]

   permissions:
     contents: read
     pages: write
     id-token: write

   jobs:
     deploy:
       runs-on: ubuntu-latest
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       steps:
         - uses: actions/checkout@v4
         - uses: actions/configure-pages@v5
         - uses: actions/upload-pages-artifact@v3
           with:
             path: .              # or a build output folder, e.g. dist/
         - id: deployment
           uses: actions/deploy-pages@v4
   ```
3. Commit it on a branch, open a PR, same as Section 2 — watch **two**
   checks now: your `lint-and-test` job from Section 2, and this `deploy`
   job (which only actually runs on `main`, per the `on: push` trigger
   above — a PR just shows it queued, not yet fired)
4. Merge it. Push to `main` triggers the `deploy` job automatically — no
   click, no manual step
5. Watch it run in the **Actions** tab, then visit
   `https://<your-username>.github.io/<repo-name>/` — that's a live URL,
   built and shipped by the merge you just made

**The payoff to say out loud:** you didn't deploy anything. You merged a
PR, and the deploy *happened to you*. That's the entire idea of CD in one
sentence.

---

## 8. Full Loop — Replay the Conflict, Now Watch Everything React

Session 1 ended with a hands-on activity: pair up, both branch off the
same line in the same file at the same time, first merge is clean, second
collides, resolve it together. Do it **again**, with the same partner —
except this time, you have a `lint-and-test` check and a `deploy` job
that Session 1 didn't. Watch what's different.

1. Same setup as Session 1's activity: partner as collaborator (if you
   dropped it, re-add them), agree on one line in one file
2. Both branch from `main` at the same time, edit that line differently,
   commit, push
3. First partner opens a PR — **watch the Checks section**: `lint-and-test`
   runs live, same as any other PR now. Merge it — and this time also
   watch the **deploy** job fire and the live site update
4. Second partner opens a PR against the now-updated `main` — conflict,
   same as before. Resolve it together, same Steps as Session 1
5. Merge the resolved PR — **two things happen automatically**: the check
   verifies the resolution didn't break anything, and the site deploys
   again with the merged result

**Say out loud what's different from Session 1:** the conflict-resolution
skill didn't change at all — what changed is everything wrapped around
it. A merge that used to just update `main` now also gets verified and
shipped, with zero extra effort from either of you. That's Sessions 1 and
2, together, doing their actual job at the same time.

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

# deploy.yml — merge to main -> live URL, no click
# Settings -> Pages -> Source: GitHub Actions, then:
name: Deploy
on:
  push: { branches: [main] }
permissions: { contents: read, pages: write, id-token: write }
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: { name: github-pages, url: ${{ steps.deployment.outputs.page_url }} }
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with: { path: . }
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## Homework Before Next Session

- [ ] Add a `.github/workflows/ci.yml` lint/test workflow to your fork of the sandbox repo
- [ ] Open a PR and watch the check run live on it
- [ ] Add a CI status badge to your fork's README
- [ ] Turn on branch protection on your fork's `main`: require the PR, require the check, require it to be up to date
- [ ] Deliberately break a test or lint rule on a branch, push it, and read the failed run before fixing it
- [ ] Add `.github/dependabot.yml` and, if a PR shows up before next session, read (don't necessarily merge) it
- [ ] Set up `.github/workflows/deploy.yml` with GitHub Pages and merge a PR — watch it deploy itself, then visit the live URL
- [ ] If you didn't finish it live: the Section 8 "Full Loop" replay with your Session 1 partner — cause a conflict again, resolve it, and watch the check and the deploy both react
