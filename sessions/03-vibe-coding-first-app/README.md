# IT Group Hub — Session 3: Vibe Coding Your First App (with Claude)

**Status:** [x] Ready

**Goal:** By the end of this session, you can start a project with Claude, tell the difference between a good prompt and a vague one, review an AI-generated diff well enough to catch a hallucination, and ship the result through the exact same branch → PR → CI loop from Sessions 1 and 2 — with Claude doing the typing.

**Contents:** [The Hook](#the-hook--why-this-is-session-3-not-session-1) · [What Vibe Coding Is](#1-what-vibe-coding-means-and-when-its-appropriate) · [Starting a Project With Claude](#2-starting-a-project-with-claudes-help) · [Prompts vs. Code](#3-iterating-on-prompts-vs-iterating-on-code) · [Reviewing AI Diffs](#4-reviewing-ai-generated-code-before-accepting-it) · [Shipping It](#5-committing-pushing-and-letting-ci--branch-protection-do-their-job) · [Failure Modes](#6-common-failure-modes) · [Hands-On Lab](#hands-on-lab) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

---

## The Hook — Why This Is Session 3, Not Session 1

Session 1 gave you history and branches as a safety net — any change, however
bad, is one `git revert` away from gone. Session 2 gave you a second safety
net — an automated check that has to pass before anything reaches `main`.
Both of those existed for one actual reason, stated back in Session 1 and now
due: **AI-assisted coding makes Git more important, not less**, because
changes get faster, larger, and easier to accept without fully reading. Today
is where that claim gets tested for real, not discussed in the abstract.

**Say this out loud before anyone touches a keyboard:** you're about to let
Claude make sweeping, fast changes on purpose. The only reason that's safe
instead of reckless is that the two things protecting you were already in
place *before* today started.

**Scope note, deliberately narrow:** the app you build today is small and
framework-free — a CLI script or a single-file page, not a React app.
Session 4 owns React/Vite properly; pulling in a framework here would make
this session about framework setup friction instead of about the actual
point, which is the Claude-partnership workflow. The tools get bigger later
(Session 4 onward); the workflow you practice today doesn't change when they
do.

**Where this is actually going:** the skills in this session — write a
clear prompt, review a diff for hallucinations, ship through CI — are not a
one-off exercise. They're the exact skills you'll use maintaining a real
church project later in this program. The scope is small today on purpose;
the workflow is the real thing.

---

## 1. What Vibe Coding Means, and When It's Appropriate

**Vibe coding** — the term, coined by Andrej Karpathy in early 2025 — means
driving development through natural-language prompts and fast iteration,
rather than hand-typing every line yourself. You describe what you want,
Claude writes it, you run it, you course-correct. The "vibe" is trusting the
loop enough to move fast — not skipping review, which is a different thing
entirely and the subject of Section 4.

**When it's a good fit:**
- Prototypes, first drafts, throwaway scripts
- Small, well-scoped tools where "does it work" is easy to verify by running it
- Anything where you'd otherwise spend most of your time on boilerplate,
  not on a hard decision

**When it needs extra scrutiny (not "don't," just "look closer"):**
- Anything touching real people's data — attendee info, payment details,
  contact lists
- Security-sensitive logic — auth checks, permission rules, anything that
  decides who can see or do what
- Code you can't easily test or verify just by running it

**The one thing this is not:** "no review." Sessions 1 and 2's discipline —
read the diff, require a passing check, get a second set of eyes — applies
exactly the same to Claude's output as it does to your own. What changes
today is *volume*, not *standards*. You'll review more code, faster, than
you're used to — which is exactly why Section 4 below exists.

---

## 2. Starting a Project With Claude's Help

Two starting points, and they call for different first moves:

| | Empty folder | Existing repo (your sandbox fork) |
|---|---|---|
| First move | Describe what you're building and let Claude propose structure | Let Claude look around first — existing patterns matter |
| Risk | Claude invents conventions with nothing to match | Claude ignores what's already there and does its own thing |

**Writing an initial prompt — describe the *what* and the constraints, not
the implementation:**

```
Bad prompt:
"Make a function called checkRSVP that loops through an array and
uses a for loop with an if statement to count yes values."

Good prompt:
"Build a single-file HTML page for a volunteer sign-up list. Plain
HTML/JS, no framework, no build step — it needs to run by just opening
the file. People can add their name to a shift; store it in
localStorage so it survives a page refresh. Keep it to one file."
```

The bad prompt dictates *how* — which defeats the point of having Claude
write it at all. The good prompt states the *what* (a sign-up list), the
*constraints* (single file, no framework, no build step, localStorage), and
leaves the implementation to Claude.

**Let Claude propose a plan before it writes code** — for anything beyond a
few lines, ask it to outline its approach first ("what's your plan before
you start writing?"). This costs one extra exchange and catches a
misunderstanding while it's still a sentence, not a diff.

---

## 3. Iterating on Prompts vs. Iterating on Code

Once Claude has written something, you have two ways to fix what's wrong —
knowing which is faster is the actual skill:

- **Redirect with a better prompt** when the *approach* is wrong, or the
  issue will recur across multiple places (e.g. "this should validate the
  phone number format everywhere it's collected, not just this one form").
- **Just edit the file yourself** when it's a one-line fix you already know
  the answer to. Round-tripping through a prompt for a typo or a wrong
  variable name is slower than typing the fix.

**Give feedback on *why*, not just "fix it":** "this breaks when the list is
empty" gets a better fix than "fix it" — Claude can't read your mind about
which edge case you noticed any better than a human collaborator could.

**Small, checkpointed asks beat one giant prompt.** "Build the whole
volunteer sign-up system with admin controls, email notifications, and a
CSV export" produces a big, hard-to-review diff and a high chance Claude
guessed wrong about something in the middle. "Build the sign-up list first"
→ review → commit → "now add removing your name" → review → commit is
slower per-step and faster overall, because every step is small enough to
actually review (Section 4) and small enough to revert cleanly if it's
wrong (Session 1's whole point).

---

## 4. Reviewing AI-Generated Code Before Accepting It

This is Session 1's diff-review discipline, applied to a much higher volume
of generated code than a human typing by hand would ever produce in the same
amount of time. The habit doesn't change. The stakes of skipping it do.

**What to actually check:**
- **Does it do what you asked** — not "does it look plausible," does it
  actually match the prompt
- **Does it match existing patterns in the repo** — if there's already a
  convention (naming, structure, how errors are handled), a good diff
  follows it instead of inventing a new one next to it
- **Anything that looks hallucinated** — an imported function, a config
  option, or an API method that doesn't actually exist. This is the
  single most distinctive Claude-authored bug category, and it's often
  confident-sounding and syntactically perfect

**Running it locally before trusting it.** Claude's confidence is not
evidence. "This should work" is not the same as "I ran it and it worked" —
the second one is what you're actually checking for, every time, the same
way you would (or should) with your own code before opening a PR.

---

## 5. Committing, Pushing, and Letting CI + Branch Protection Do Their Job

This is the loop closing — Session 1's mechanics and Session 2's required
check, exercised on a real PR from work you did today, with Claude doing
most of the typing:

```bash
git checkout -b add-volunteer-signup
# ... Claude writes the file, you review it (Section 4) ...
git add .
git commit -m "Add volunteer sign-up list page"
git push -u origin add-volunteer-signup
# open a PR — same as Session 1, Section 5
# watch the lint-and-test check run — same as Session 2, Section 2
```

**Small, frequent commits — the muscle memory from Session 1 — still
applies, even though Claude is doing the typing.** A single commit
containing "the whole feature" is exactly as hard to review, revert, or
bisect when Claude wrote it as when a human did. Commit at the same
granularity you would if you were typing it yourself: one logical change
per commit, not one commit per session.

**The check doesn't know or care who wrote the diff.** That's the entire
point of Session 2 existing before this one — `lint-and-test` runs the same
way, finds the same category of problems, whether the code came from your
keyboard or Claude's.

---

## 6. Common Failure Modes

Set expectations before they hit one, not after:

| Failure mode | What it looks like | The fix |
|---|---|---|
| **Confident hallucination** | Claude uses an import, method, or config option that doesn't exist — written with the same confidence as code that's correct | Run it. It fails immediately, loudly, and is easy to catch *if you actually run it* before trusting it |
| **Rubber-stamping a big diff** | A diff "looks right" at a glance, gets approved without being read, because it's long and reading it feels slow | Smaller, checkpointed asks (Section 3) make this less likely to happen in the first place |
| **Vague prompt, vague result** | A one-line prompt with no constraints gets back something over-engineered, under-scoped, or just not what you meant | State the *what* and the *constraints* explicitly (Section 2) — Claude fills gaps with guesses, and guesses are what you're trying to avoid |

---

## Hands-On Lab

Each attendee (or pair) picks — or is assigned — a small, scoped,
**church-relevant** tool to build with Claude against their sandbox fork.
Same technical scope throughout this session (no framework, no backend) —
just not generic. This is the first session that should feel like "I build
things for the church," not three months from now once React and Firebase
show up:

- **A CLI script** — e.g. an RSVP tally (read a text list of yes/no
  responses, print a headcount), or a volunteer roster formatter (read a
  CSV of names/roles, print a formatted sign-up sheet)
- **A single-file HTML/JS page** — e.g. a volunteer sign-up list, an event
  RSVP counter, or a simple service-setup checklist — using `localStorage`
  if it needs to remember anything, no backend needed yet

**Constraint that matters more than the idea itself: it must ship as a real
PR**, checked by the CI workflow from Session 2, reviewed by a partner
using Session 1's review habits. The artifact is secondary to practicing
the full loop once, end to end, with Claude doing the typing.

**Suggested flow for the lab:**
1. Pick the tool, write the initial prompt together as a pair (Section 2)
2. Let Claude propose a plan, then build it in small, checkpointed asks (Section 3)
3. Review the diff together before committing (Section 4) — deliberately
   look for at least one thing to question, even if it turns out fine
4. Commit, push, open a PR, watch the check run (Section 5)
5. Partner reviews and approves, merge it

---

## Quick Reference Card (keep this open while working)

```
# good prompt vs. vague prompt
Vague:  "make a signup form"
Good:   "Build a single-file HTML page for a volunteer sign-up list.
         Plain HTML/JS, no framework, no build step. Store entries in
         localStorage. Keep it to one file."
        -> states the WHAT and the CONSTRAINTS, leaves the HOW to Claude

# red flags when reviewing a Claude diff
- an import, method, or config option you don't recognize -> did you
  check it actually exists?
- matches what you asked, but not how the rest of the repo does things
- "this should work" energy, with no actual local run to back it up
- a diff so big you're skimming instead of reading

# the loop, same as Sessions 1 & 2, Claude typing instead of you
git checkout -b <branch-name>
# Claude writes it, you review it
git add .
git commit -m "message"            # small, checkpointed, not one giant commit
git push -u origin <branch-name>
# open PR -> watch the check run -> partner reviews -> merge
```

---

## Homework Before Next Session

- [ ] Extend the tool built in-session with one more small feature, same PR discipline (branch → Claude → review → PR → CI → merge)
- [ ] Deliberately spot-check one Claude-authored diff for a hallucinated API/method before running it
- [ ] Write one vague prompt and one good prompt for the same small task, and notice the difference in what comes back
