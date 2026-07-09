# IT Group Hub — Session 1: Git Basics to Your First PR

**Status:** [x] Ready

**Goal:** By the end of this session, you can fork a repo, clone it, make a change, push it, open a PR, and resolve a simple merge conflict — all by hand, no AI assistance. This is the muscle memory that AI tools will later automate for you, but you should understand what's happening underneath first.

**Contents:** [Why Git Exists](#why-git-exists--the-problem-before-version-control) · [Setup Check](#0-setup-check-do-before-session-or-first-5-min) · [Fork vs. Clone](#1-fork-vs-clone--whats-the-difference) · [npm Packages](#15-npm-packages--what-happens-right-after-you-clone) · [Local Basics](#2-local-basics--just-enough-to-orient) · [Branching](#3-branching) · [Push](#4-push) · [Open a PR](#5-open-a-pull-request-pr) · [Code Review](#6-code-review-basics) · [Conflict Resolution](#7-simple-conflict-resolution-no-rebase-just-merge) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

---

## Why Git Exists — The Problem Before Version Control

Before diving into commands, it helps to feel the pain Git was built to solve.
Ask the room: has anyone worked with files like these?

```
proposal.docx
proposal_v2.docx
proposal_v2_edited.docx
proposal_FINAL.docx
proposal_FINAL_v2.docx
proposal_FINAL_v2_ACTUALLY_FINAL.docx
proposal_FINAL_v2_ACTUALLY_FINAL_useThisOne.docx
```

This is how file versioning worked (and often still works) without a proper
version control system — manual naming conventions, shared drives, emailing
files back and forth, USB sticks, "did you get my latest copy?" This breaks
down fast:

- **No real history** — you can't see *what* changed between versions, only that a new file exists
- **No safe collaboration** — two people editing the same file at the same time means someone's changes get overwritten, or you end up with `proposal_v2_JOHN.docx` and `proposal_v2_MARIA.docx` that now need to be manually merged by eye
- **No accountability** — who changed what, and why, gets lost immediately
- **No safe experimentation** — there's no cheap way to "try something" without risking the working version, so people either don't experiment or they duplicate the whole file "just in case"
- **Fragile "final" concept** — "final" is really just whoever renamed the file last

**Git solves all of this:**
- Every change is tracked with *who* changed it, *when*, and *what exactly* changed (down to the line)
- Multiple people can work on the same files at the same time, safely, using branches
- You can always go back to any previous point in history — no need to keep manually renamed backup copies
- "Merging" is a real, structured process (Section 7 below) instead of manually eyeballing two files and copy-pasting the right bits

### A Quick Word on CVS and SVN — the Step Before Git

Git wasn't the first version control system — it's worth knowing what came
before, especially for anyone who's worked in older IT shops:

- **CVS (Concurrent Versions System)** — one of the earliest widely-used
  version control tools. Tracked file history and allowed multiple people to
  work on a codebase, but had a **centralized** model: there was one single
  server holding the "real" history, and everyone talked directly to it.
- **SVN (Subversion)** — came after CVS as an improvement (better handling
  of renames, directory versioning, atomic commits), but kept the same
  **centralized** model — still one central server as the single source of truth.

**The centralized model's core limitation:** you needed a constant connection
to the central server to commit, see history, or create most branches.
Branching and merging in SVN was heavy and often avoided in practice — teams
would work directly on a shared trunk rather than branch freely, because
merging branches back together was painful.

**What Git changed — distributed version control:**
- Every clone is a **full copy of the entire history** — no constant connection to a central server needed
- Branching and merging are cheap and fast, which is why Git-based workflows (branch → PR → merge) are actually usable day-to-day, unlike heavy SVN branching
- This is *why* the fork/clone/branch workflow you're about to learn is even possible the way it is — it's a direct consequence of Git being distributed, not centralized

If you ever hear someone reference "the good old days of SVN conflicts,"
this is why — centralized version control made exactly the kind of safe,
frequent branching we're about to practice much harder to do well.

### Why This Matters Even More in the Age of Vibe Coding

Here's the part that ties this history directly to why we're doing this
hub at all: **AI-assisted coding makes Git more important, not less.**

Think about what changes when you code with Claude instead of typing every
line by hand:
- Changes happen **faster** — an AI can rewrite a whole file in seconds, far
  faster than the manual-file-naming era or even a solo human coder
- Changes can be **larger** — an AI assistant might touch many files at once
  in a single request
- It's **easier to accept something you haven't fully reviewed** — the
  convenience of AI-generated code makes it tempting to skip the careful
  read-through

Every one of those makes Git's core guarantees *more* valuable, not less:

- **History as a safety net** — if an AI-assisted change breaks something,
  Git lets you see exactly what changed and revert it, the same way it
  would for a human-made change. Without version control, an AI mistake is
  just as unrecoverable as the old `_FINAL_v2` file chaos — except it
  happened in seconds instead of over weeks.
- **Branches as a sandbox** — you can let Claude make sweeping changes on a
  branch, review the diff, and throw it away entirely if it's wrong, with
  zero risk to your working code. This is what makes "vibe coding" safe to
  do at all rather than reckless.
- **Diffs as the review mechanism** — reading a Git diff is *how* you review
  AI-generated code responsibly. The PR/code-review workflow you're about to
  learn isn't just for human-to-human collaboration — it's the exact same
  discipline you'll apply when reviewing what Claude wrote for you.
- **Commits as accountability** — even when Claude writes the code, *you*
  are the one committing it. Git keeps that responsibility clear and
  auditable, which matters more, not less, as more code gets AI-generated.

### If We Were Still on SVN, None of This Would Work

This isn't just "Git is nicer than SVN" — walk through what vibe coding and
agentic workflows actually *require*, and check it against SVN's centralized
model:

- **Instant, local commits with no network round-trip.** AI-assisted
  iteration means committing constantly — sometimes every few seconds — to
  create checkpoints you can fall back to. In Git that's a local, offline,
  sub-second operation. In SVN, every commit *is* a write to the shared
  central server; there's no local history to checkpoint against. Rapid-fire
  AI iteration would either hammer the central server or, more realistically,
  nobody would bother — and the safety net disappears.
- **Cheap, disposable branches.** "Let Claude go wild on a branch, review the
  diff, throw it away if it's wrong" only works because Git branches are
  free and local. SVN branching is heavy and server-side, and merging back
  was painful enough that teams avoided it entirely and worked directly on a
  shared trunk. An AI agent proposing a throwaway experimental branch every
  time it tries something would have been a non-starter, both mechanically
  and culturally.
- **Multiple parallel agent sessions on separate branches (`git worktree`).**
  Running several Claude sessions at once, each on its own branch and
  working copy, is a natural extension of Git being distributed. SVN's
  centralized, trunk-heavy workflow made even *one* long-lived branch
  expensive — running several in parallel purely for AI experimentation
  would have been impractical.
- **Reverting a bad AI change in seconds.** `git revert` / `git reset` are
  local and instant. Undoing a change in SVN means operating against the
  shared central history — slower and riskier — so every "try it, back out
  if it's wrong" cycle carries more weight and more hesitation.

**The takeaway:** vibe coding and agentic workflows don't just work *better*
with Git — they depend on properties (local commits, cheap branches, easy
parallel worktrees, instant revert) that a centralized system like SVN
never had. If this hub were still running on SVN, most of what Session 3
and Session 11 teach either wouldn't work the way it's designed, or would be
painful enough in practice that no one would actually do it.

In short: the distributed, branch-heavy, diff-reviewable model Git introduced
over CVS/SVN is exactly the infrastructure that makes AI-assisted development
trustworthy — and even *possible* in the way we're about to practice it —
rather than chaotic. Session 3 (Vibe Coding) and Session 11 (Agentic
workflows) both lean directly on the Git fundamentals from today — this
isn't a side skill, it's the foundation the rest of the hub sits on.

**A concrete example, right here:** the way this very curriculum was built —
iterating with Claude turn by turn, adding a topic, committing, adding
another, committing again, a dozen small changes in sequence — is itself a
demonstration of the point. Without Git, that process would mean re-sending
whole files back and forth, manually tracking which version had which
addition, and hoping nothing got overwritten (exactly the `_FINAL_v2` chaos
from earlier, just at AI speed instead of human speed). With Git, every
iteration is a clean, reviewable, revertable commit. **What we're doing right
now to build this hub would be largely impossible, or painfully slow, without
version control.** That's not a hypothetical — it's the actual mechanism
behind the repo you'll be working in.

**Advanced/optional — `git worktree`:** as you get further into AI-assisted
and agentic workflows (Session 11), you'll often want to work on more than
one branch *at the same time* — for example, letting an AI agent work on one
branch while you keep your main working copy untouched on another, without
constantly stashing or switching. `git worktree` lets you check out multiple
branches into separate folders simultaneously from the same repo, instead of
one branch at a time in one folder. Not needed for today's basics, but worth
knowing the name now — we'll come back to it hands-on when we get to agentic
workflows, where running multiple parallel Claude sessions on different
branches becomes genuinely useful.

Keep this comparison in mind as we go through the technical steps — every
Git concept below exists specifically to solve one of the problems in that
file-naming mess, and several exist specifically because Git chose a
distributed model over the CVS/SVN centralized one.

---

## 0. Setup Check (do before session or first 5 min)

- [ ] GitHub account created
- [ ] Git installed (`git --version` in terminal)
- [ ] Git identity configured:
  ```
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```
- [ ] SSH key or GitHub CLI auth set up (ask facilitator if unsure)
  - Quickest path if you're stuck: install the [GitHub CLI](https://cli.github.com/) and run `gh auth login` — it handles SSH/HTTPS credentials for you, no manual key setup needed.

---

## 1. Fork vs. Clone — What's the Difference?

| | Fork | Clone |
|---|---|---|
| What it does | Makes **your own copy** of a repo on GitHub (under your account) | Downloads a copy of a repo (yours or anyone's) to **your local machine** |
| Where it lives | GitHub.com | Your computer |
| When you use it | When you don't have write access to the original repo (e.g. contributing to someone else's project) | Always — you need it locally to actually edit files |
| Typical flow | Fork → then clone **your fork** | Clone → edit → push |

**Why this matters for us:** For church projects, you'll likely fork the repo first (since you won't have direct push access to the main repo yet), then clone *your fork* to your machine to work on it.

### Steps: Fork
1. Go to the repo on GitHub
2. Click **Fork** (top right)
3. GitHub creates `your-username/repo-name` under your account

### Steps: Clone
```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

---

## 1.5 npm Packages — What Happens Right After You Clone

Most repos you clone won't run immediately — they depend on external packages
that aren't stored in Git itself. This is the first thing you'll hit after
cloning, so it's worth understanding now.

```bash
npm install    # reads package.json and package-lock.json, downloads dependencies into node_modules/
```

**Key files:**

| File | Committed to Git? | What it is |
|---|---|---|
| `package.json` | Yes | The list of dependencies your project needs, plus scripts (`npm run dev`, etc.) |
| `package-lock.json` | Yes | The *exact* versions of every dependency (and their dependencies) actually installed — ensures everyone gets identical versions |
| `node_modules/` | **No** — gitignored | The actual downloaded package code — can always be regenerated from the two files above, so there's no reason to commit it (it's huge and machine-specific) |

**Why `node_modules` is gitignored:** this connects directly back to what we covered — Git tracks *source of truth*, not *regeneratable output*. `package.json` + `package-lock.json` are the source of truth; `node_modules` is just the result of running `npm install` against them, the same way a build folder is the result of compiling source code. Committing it would bloat the repo for no benefit.

**dependencies vs. devDependencies:**
- `dependencies` — needed to actually run the app (e.g. React itself)
- `devDependencies` — only needed while developing (e.g. a linter, a test runner) — not shipped to production

**Practical flow after cloning any repo:**
```bash
git clone <url>
cd <repo>
npm install     # always do this before trying to run anything
npm run dev      # or whatever the project's start script is (check package.json "scripts")
```

If `npm install` fails or acts strange, check your Node.js version first —
many projects require a specific major version (check for an `.nvmrc` file
or the `engines` field in `package.json`).

---

## 2. Local Basics — Just Enough to Orient

```bash
git status       # what's changed, what's staged
git add <file>   # stage a specific file
git add .        # stage everything changed
git commit -m "short, clear message describing the change"
git log          # see commit history
git log --oneline   # compact version
```

**Rule of thumb for commit messages:** describe *what* changed and *why*, not "fixed stuff." Example: `Fix null check on student enrollment form`.

---

## 3. Branching

**Why branches exist:** isolate your work so you don't break `main` while you're still figuring things out. Everyone works on their own branch, then merges in through a PR.

```bash
git branch                        # list branches, see which one you're on
git checkout -b my-feature-name   # create AND switch to a new branch
git checkout main                 # switch back to main
```

**Naming convention:** short, descriptive, hyphenated. e.g. `fix-login-button`, `add-student-search`.

---

## 4. Push

```bash
git push -u origin my-feature-name   # first push of this branch (-u sets tracking)
git push                              # subsequent pushes, once tracking is set
```

If you forget `-u` the first time, Git will tell you exactly what command to run — just copy-paste it.

---

## 5. Open a Pull Request (PR)

1. Push your branch (above)
2. Go to your fork on GitHub — you'll usually see a **"Compare & pull request"** banner
3. Click it, or go to **Pull Requests → New Pull Request**
4. Fill in:
   - **Title:** short summary of the change
   - **Description:** what you changed, why, and how to test it (fill the PR template if one exists)
5. Click **Create Pull Request**
6. Request a reviewer if you have one assigned

---

## 6. Code Review Basics

**As the author:**
- Read your own diff before requesting review — catch typos/debug logs yourself first
- Respond to every comment (even just "done" or "good catch")

**As the reviewer:**
- Read the diff, not just the description
- Leave comments on specific lines
- Choose: **Comment** (just a note) / **Approve** / **Request changes** (blocking, needs a fix)
- Be specific: "this could cause a null error if X is empty" is more useful than "this looks off"

---

## 7. Simple Conflict Resolution (no rebase, just merge)

**What a conflict is:** two branches changed the *same lines* of the same file, and Git can't automatically decide which version is correct — so it asks you.

### Steps

1. Make sure your branch is up to date with the latest `main`:
   ```bash
   git checkout main
   git pull
   git checkout my-feature-name
   git merge main
   ```
2. If there's a conflict, Git will tell you which file(s) are affected. Open the file — you'll see markers like this:
   ```
   <<<<<<< HEAD
   your version of the code
   =======
   the incoming version of the code
   >>>>>>> main
   ```
3. **Read both versions.** Decide what the final correct code should be — it might be one side, the other, or a combination of both.
4. **Manually edit the file:** delete the `<<<<<<<`, `=======`, and `>>>>>>>` markers, and leave only the correct final code.
5. Save the file, then:
   ```bash
   git add <the resolved file>
   git commit -m "Resolve merge conflict in <file>"
   git push
   ```

**Note:** This is intentionally the *manual* way. Merge tools in your editor (VS Code, etc.) can help highlight conflicts, but you should be able to read and resolve the raw markers by hand — this is often where AI tools and GUI clients oversimplify or get it wrong.

---

## Quick Reference Card (keep this open while working)

```
git clone <url>
cd <repo>
npm install               # install dependencies before doing anything else
git checkout -b <branch-name>
git add .
git commit -m "message"
git push -u origin <branch-name>

# Getting latest main into your branch
git checkout main
git pull
git checkout <branch-name>
git merge main
# (resolve conflicts if any, then:)
git add <file>
git commit -m "Resolve merge conflict"
git push
```

---

## Homework Before Next Session

- [ ] Fork the practice repo — see [`/sandbox`](../../sandbox) for the shared repo used across sessions. **Facilitator note:** the sandbox repo is still TBD (see [`sandbox/README.md`](../../sandbox/README.md)) — confirm and share the actual fork link before assigning this homework.
- [ ] Clone your fork locally
- [ ] Run `npm install` and get the project running locally
- [ ] Make one small change, commit it, push it, open a PR
- [ ] If comfortable, try deliberately creating a conflict with a partner and resolving it together
