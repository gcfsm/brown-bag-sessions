# IT Group Hub — Session 1: Git Basics to Your First PR

**Status:** [x] Ready

**Goal:** By the end of this session, you can fork a repo, clone it, make a change, push it, open a PR, and resolve a simple merge conflict — all by hand, no AI assistance. This is the muscle memory that AI tools will later automate for you, but you should understand what's happening underneath first.

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

Keep this comparison in mind as we go through the technical steps — every
Git concept below exists specifically to solve one of the problems in that
file-naming mess.

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

- [ ] Fork the practice repo (link: _______________)
- [ ] Clone your fork locally
- [ ] Make one small change, commit it, push it, open a PR
- [ ] If comfortable, try deliberately creating a conflict with a partner and resolving it together
