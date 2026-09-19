# GITCom — Session 3: Vibe Coding Your First App (with Claude)

**Status:** [x] Ready

**Goal:** By the end of this session, you can start a project with Claude, tell the difference between a good prompt and a vague one, review an AI-generated diff well enough to catch a hallucination, and ship the result through the exact same branch → PR → CI loop from Sessions 1 and 2 — with Claude doing the typing.

**Contents:** [The Hook](#the-hook--why-this-is-session-3-not-session-1) · [What Vibe Coding Is](#1-what-vibe-coding-means-and-when-its-appropriate) · [Starting a Project With Claude](#2-starting-a-project-with-claudes-help) · [Prompts vs. Code](#3-iterating-on-prompts-vs-iterating-on-code) · [Reviewing AI Diffs](#4-reviewing-ai-generated-code-before-accepting-it) · [Shipping It](#5-committing-pushing-and-letting-ci--branch-protection-do-their-job) · [Failure Modes](#6-common-failure-modes) · [Hands-On Lab](#hands-on-lab) · [Skills](#7-making-claude-fit-how-you-work-skills) · [Skill Feedback Loop](#8-keeping-your-skills-sharp-the-feedback-loop) · [Routines](#9-work-that-runs-without-you-routines) · [Act II Lab](#hands-on-lab--act-ii-make-a-skill-then-improve-it) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Retrospective](#session-retrospective--treat-the-session-like-a-sprint) · [Homework](#homework-before-next-session)

---

## The Hook — Why This Is Session 3, Not Session 1

**Deck:** [Slides 1–4](slides.html#s1)

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

**Deck:** [Slides 5–6](slides.html#s11)

**Vibe coding** — the term, coined by Andrej Karpathy in early 2025 — means
driving development through natural-language prompts and fast iteration,
rather than hand-typing every line yourself. You describe what you want,
Claude writes it, you run it, you course-correct. The "vibe" is trusting the
loop enough to move fast — not skipping review, which is a different thing
entirely and the subject of Section 4.

**Claude can work across the whole range.** The old version of this session
split work into "good fit" and "needs extra scrutiny." That understates what
the tool can do. The useful distinction is now how thoroughly we verify the
result before shipping:

- With fast-feedback work, prototype, run focused tests, and review the visible
  behavior.
- With real people's data, add privacy and access tests.
- With auth or payments, add adversarial review. For systems that are difficult
  to exercise locally, use evals and production monitoring.

Higher stakes need more checks, not a different conclusion about whether
Claude belongs in the workflow.

**Separate the author from the reviewer.** Claude can write the change and
perform an adversarial pass over its own work. Then use a different model,
such as Gemini in GitHub, to review the PR independently. The models can find
different failure modes, but neither owns the decision: read their findings,
require passing checks, and keep the merge with a human.

---

## 2. Starting a Project With Claude's Help

**Deck:** [Slides 7–8](slides.html#s13)

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
"Build a volunteer sign-up page. Plain HTML/JS, no framework, no build
step — it should run by just opening the file. People add their name
to a shift; store it in localStorage so it survives a refresh."
```

The bad prompt dictates *how* — which defeats the point of having Claude
write it at all. The good prompt states the *what* (a sign-up page), the
*constraints* (no framework, no build step, runs by just opening the file,
localStorage), and leaves the implementation to Claude.

**Say this out loud when you show the good prompt.** Look at what writing it
actually required: knowing that a framework is optional, that a build step is
a thing you can decline, and that `localStorage` survives a page refresh.
Those aren't wording choices — they're technical knowledge, and a beginner
couldn't have produced that prompt. Claude wrote the code; someone still had
to know what to ask for.

That's the honest answer to "does this mean I don't need to learn to code
anymore." No — it moves where your knowledge gets applied. It stops being
about typing syntax from memory and starts being about knowing what to ask
for, and recognising a wrong answer when you see one. Which is what the other
nineteen sessions are for. On the slide, the three phrases that took knowing
something are highlighted in gold.

**Point Claude at existing building blocks — don't hand-roll what already
exists.** The same knowledge that makes a good prompt also tells you what
*not* to ask Claude to build. An accessible dropdown, a date picker, a modal,
form-validation UI — these are solved problems, and a hand-rolled version is
usually subtly broken in ways a glance won't catch: keyboard navigation,
focus traps, screen-reader labels. The move is to point Claude at a
battle-tested library instead of asking it to reinvent one — less code to
review, and the hard edge cases arrive already handled.

For React specifically, the name worth knowing is
[**shadcn/ui**](https://ui.shadcn.com) — accessible, composable components you
copy straight into your project. It needs React and a build step, so the
hands-on version belongs to Session 4's world, not today's single-file lab
(which stays dependency-free on purpose, so the session stays about the
workflow and not about setup). But the *instinct* starts now: before you ask
Claude to build a component, ask whether a good version already exists. That
question — "is this already a solved problem?" — is itself part of the
development skill this session is really teaching.

**Let Claude propose a plan before it writes code** — for anything beyond a
few lines, ask it to outline its approach first ("what's your plan before
you start writing?"). This costs one extra exchange and catches a
misunderstanding while it's still a sentence, not a diff.

**Aside: match the model to the task.** Once you're working across more than
one Claude model, the same "know what to ask for" instinct from above applies
to *which model* you hand the work to, not just how you phrase the prompt:

- **Planning and genuinely complex work** (architecture decisions, tricky
  bugs, anything where a wrong first move is expensive to unwind) — reach for
  the strongest model available (e.g. Opus).
- **Mechanical, well-specified work** (renaming, boilerplate, applying a
  pattern you've already decided on) — a faster, cheaper model (e.g. Sonnet
  or Haiku) does it just as well, faster and for less.

You don't need to think hard about this every time — as a rule of thumb,
plan with your strongest model, then delegate the mechanical follow-through
to a lighter one. This matters more as your usage grows; keep it in the back
of your mind for now.

---

## 3. Iterating on Prompts vs. Iterating on Code

**Deck:** [Slide 9](slides.html#s16)

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

**Deck:** [Slide 10](slides.html#s17)

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

**Deck:** [Slide 11](slides.html#s19)

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

**Deck:** [Slide 12](slides.html#s20)

Set expectations before they hit one, not after:

| Failure mode | What it looks like | The fix |
|---|---|---|
| **Confident hallucination** | Claude uses an import, method, or config option that doesn't exist — written with the same confidence as code that's correct | Run it. It fails immediately, loudly, and is easy to catch *if you actually run it* before trusting it |
| **Rubber-stamping a big diff** | A diff "looks right" at a glance, gets approved without being read, because it's long and reading it feels slow | Smaller, checkpointed asks (Section 3) make this less likely to happen in the first place |
| **Vague prompt, vague result** | A one-line prompt with no constraints gets back something over-engineered, under-scoped, or just not what you meant | State the *what* and the *constraints* explicitly (Section 2) — Claude fills gaps with guesses, and guesses are what you're trying to avoid |

---

## Hands-On Lab

**Deck:** [Slides 13–14](slides.html#s21)

**The default task: a volunteer sign-up page.** Everyone builds the same
thing unless they'd rather not — a shared task means a pair that gets stuck
can look sideways, and it makes the review step comparable across the room.

Work in your sandbox fork, on a branch:

```bash
git checkout -b volunteer-signup
claude
```

Then give Claude the "Good" prompt from Section 2, word for word. That's
deliberate: they've already seen it, discussed why it's good, and now they
watch it work. Nobody should be staring at a blank prompt wondering what to
type.

**Done when all three are true:**

1. The page opens by double-clicking the file — no server, no build step
2. A name added to a shift is still there after a refresh
3. The PR is open, CI is green, and a partner has approved it

Point 3 matters more than the artifact. The tool is small on purpose; what's
being practised is the full loop once, end to end, with Claude doing the
typing.

**If a pair wants their own idea**, anything the same size works — an RSVP
tally that reads yes/no responses and prints a headcount, or a roster
formatter that reads a CSV and prints a sign-up sheet. Same rules: no
framework, no backend, ships as a PR.

**Suggested flow for the lab:**
1. Pick the tool, write the initial prompt together as a pair (Section 2)
2. Let Claude propose a plan, then build it in small, checkpointed asks (Section 3)
3. Review the diff together before committing (Section 4) — deliberately
   look for at least one thing to question, even if it turns out fine
4. Commit, push, open a PR, watch the check run (Section 5)
5. Partner reviews and approves, merge it

**That's Act I — the one-off loop, shipped once.** Once the room has done it
end to end, move to Act II below: the same partnership, but made durable so
nobody starts from a blank prompt next time.

---

## Beyond the One-Off Loop (Act II)

**Deck:** [Slide 15](slides.html#s23)

The loop in Sections 1–5 works every time — but it forgets you the moment the
session ends. Every new session, you re-explain the stack, the conventions,
the way you like commits written. Act II is the fix, in three steps that build
on each other:

```
the one-off loop  ->  a skill it remembers  ->  a routine that starts itself
```

This is the part worth doing **in the room, on their own machines** — by the
end of the session everyone should have a working skill set up, not just a
description of one.

---

## 7. Making Claude Fit How You Work (Skills)

**Deck:** reference notes only

A **skill** is a small folder of knowledge — a `SKILL.md` file — that Claude
picks up **only when it's relevant**, and ignores the rest of the time. That
"only when relevant" is the whole point, and it connects straight back to the
context "desk" from Slide 5:

| | Lives where | When it's read | Good for |
|---|---|---|---|
| **`CLAUDE.md`** | repo root | *Always* — on the desk every message, counts against context every time | The few things always true: the stack, how to run it |
| **A skill** | `.claude/skills/<name>/SKILL.md` | *On demand* — pulled off the shelf only when its description matches | Knowledge you need *sometimes*: "how we build for the church" |

Putting everything in `CLAUDE.md` bloats every message; a skill keeps the
knowledge available without paying for it until it's needed.

**Anatomy of a skill** — it's just a Markdown file with a short frontmatter
header:

```
---
name: church-conventions
description: How we build GCF apps — stack, naming, review rules.
             Use for any church project.
---
Firestore for data. No frameworks in single-file tools.
Every PR needs a passing check and a second reviewer…
```

**The `description` is the trigger.** It is not decoration — it is the *only*
thing Claude uses to decide whether to reach for this skill. A vague
description means the skill never fires; a sharp one ("use for any church
project") means it fires exactly when you want it. This is the single most
important line in the file, and Section 8 is entirely about tuning it.

**How to make one:** run `/skills` and follow the prompts, or just ask Claude
— "write me a skill that captures how we build church apps." Because a skill
is a file in the repo, it ships through the same branch → PR → review loop as
any other change, which means the *team's* conventions can live in version
control instead of in one person's head.

---

## 8. Keeping Your Skills Sharp (the Feedback Loop)

**Deck:** reference notes only

A skill is never right the first time, and that's expected. The skill that
matters is not writing one — it's **improving it when it misfires**, the same
way Section 3 taught you to iterate on prompts. Three failure shapes, and what
each one means:

| What happened | What it usually means | The fix |
|---|---|---|
| **It didn't trigger** | Claude ignored a skill that clearly applied | The `description` didn't match how you actually asked — rewrite it in the words you really use |
| **It triggered, wrong result** | The instructions inside were vague or wrong | Say *why* it was wrong (Section 3's rule), then edit the body so the next run starts correct |
| **It triggers too often** | The `description` is too broad | Narrow it — name the specific situation it's for |

**Why this is worth the habit:** a one-off correction dies when the session
clears. A fix to the skill is **banked** — it applies from now on, for
everyone who has the skill. Corrections stop evaporating and start
accumulating.

**The power tools (named now, taught in Session 11):** the `skill-creator`
skill can draft, test, and optimise a skill's description against real
examples, and `/skill-doctor` diagnoses *why* a skill isn't triggering. You
don't need either today — the manual loop (use it, watch it miss, tighten it)
is the point. Just know the tooling exists for when a skill earns it.

---

## 9. Work That Runs Without You (Routines)

**Deck:** [Slides 15–16](slides.html#s23)

A **routine** is the whole loop from today, running with **nobody at the
keyboard**. It's a saved prompt plus the repositories, cloud environment, and
connectors it's allowed to touch. It runs on Anthropic's infrastructure on a
schedule or in response to an event, so it fires with your laptop shut.

Two things have to be said out loud before anyone creates one:

- **It runs with no permission prompts.** Whatever you granted it, it will use
  — writes included. In a normal session Claude stops to ask; a routine does
  not. So the lesson here is **scoping, not scheduling**: give it only the
  repositories and connectors it actually needs, and nothing more.
- **It acts as you.** Its commits, pull requests, Slack messages, and tickets
  carry *your* identity. A routine's mistake is your mistake, with your name on
  it. That's not a reason to avoid them — it's the reason to scope them tightly.

**Where a routine ends and CI begins** (this trips people up): Session 2's CI
is a *deterministic gate* — same input, same answer, and it blocks the merge.
A routine is *judgment* — it reads, decides, and **proposes**. They are not
interchangeable. A routine is great for "unattended, repeatable, clear
outcome" work — a weekly issue triage, a weekly security scan — but it should
**never be the check that has to pass**. Keep the gate deterministic; let the
routine suggest.

We'll set a simple one up together in the lab. The deeper, tool-calling
version — a routine that fires a custom MCP server you built — is **Session
11**, where it lands properly: a routine is what happens once you've given
Claude real tools to run, not just instructions to read.

### The Abyss self-healing routine

Abyss now uses this pattern for production runtime errors. Present it as a
real example of a tightly scoped routine, not as a promise that an agent can
safely operate without boundaries:

1. Abyss fingerprints repeated frontend error-boundary and Cloud Function
   failures into incidents instead of treating every occurrence as new.
2. The incident gains a redacted stack, occurrence count, affected module,
   and an independent server-log count. A read-only, environment-scoped MCP
   connector exposes that evidence to the routine.
3. An hourly routine reads production incidents and judges whether one is a
   breaking or blocking failure. Non-urgent verdicts are recorded so the next
   run does not pay to judge the same incident again.
4. For one eligible incident, one Claude fixer produces the smallest repair
   and runs the repository's full verification gate. A separate Claude pass
   tries to break the diff and may send it back for one revision. Gemini then
   reviews the resulting PR independently in GitHub.
5. If the repair survives, the routine opens one hotfix PR and stops. It never
   merges and never deploys; a human keeps both decisions.

**Say this out loud:** the useful part is not "AI fixes production." The useful
part is the boundary around the judgment: production runtime errors only,
owned repositories only, at most three agents, one PR per incident, and a hard
stop before merge or deploy. Incident text is data, not instructions.

**Current implementation:** the pipeline and `/self-heal` playbook landed in
Abyss across issues #1128 and #1168. The latest follow-up also moves legacy
`alerted` incidents back into the filing queue on recurrence, so active errors
repair their own queue state without a one-off backfill.

> **Facilitator note — research preview.** Routines are evolving; specific
> screens, limits, and the exact `/schedule` commands may have moved by the
> time you teach this. Teach the *shape* (saved prompt + scope + trigger, runs
> as you, proposes rather than gates); demo the current UI live rather than
> from a screenshot that will age.

**Product guidance checked 2026-09-18:** Anthropic's current help pages describe
[Claude and Cowork as a gradually merging experience](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude),
list [`low`, `medium`, `high`, `xhigh`, `max`, and `auto` as Claude Code effort
choices](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips),
and advise checking the account's Usage page because
[limits vary by plan](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work).
On the current Max (20x) account, that page shows three meters: the rolling
5-hour limit, **Weekly · all models**, and a separate **Weekly · Fable** meter.
Recheck these screens before presenting a later session.

---

## Hands-On Lab — Act II: Make a Skill, Then Improve It

**Deck:** reference notes only

Everyone, on their own machine, in their sandbox fork:

1. **Create a small skill.** Run `/skills` and make something genuinely useful
   and small — a `commit-style` skill capturing how you want commit messages
   written is a good default (short imperative subject, why-not-what body).
2. **Use it on a real change** — make any small edit and let Claude write the
   commit. Watch whether the skill triggers *on its own*, without you naming
   it.
3. **Improve it.** It missed, or wrote the message wrong? Tighten the
   `description` (so it triggers) and the instructions (so it's right), then
   do another commit and confirm it's better.

**Done when:** your skill triggers on its own for the right task, and you've
improved it at least once from watching it work.

**Then, together as a room:** set up *one* routine — something small and
obviously safe, scoped to a single sandbox repo — so everyone sees the scoping
decision made deliberately, out loud, before anything runs as them.

---

## Quick Reference Card (keep this open while working)

**Deck:** none — reference material

```
# good prompt vs. vague prompt
Vague:  "make a signup form"
Good:   "Build a volunteer sign-up page. Plain HTML/JS, no framework,
         no build step, runs by opening the file. Store entries in
         localStorage so they survive a refresh."
        -> states the WHAT and the CONSTRAINTS, leaves the HOW to Claude

# red flags when reviewing a Claude diff
- an import, method, or config option you don't recognize -> did you
  check it actually exists?
- matches what you asked, but not how the rest of the repo does things
- "this should work" energy, with no actual local run to back it up
- a diff so big you're skimming instead of reading

# before asking Claude to BUILD a component, ask if it already exists
- hand-rolled dropdown / date picker / modal -> usually subtly broken
  (keyboard nav, focus traps, screen-reader labels)
- "use a battle-tested library instead" -> less to review, a11y handled
- React later? shadcn/ui (Session 4). one file today? stay dependency-free

# the loop, same as Sessions 1 & 2, Claude typing instead of you
git checkout -b <branch-name>
# Claude writes it, you review it
git add .
git commit -m "message"            # small, checkpointed, not one giant commit
git push -u origin <branch-name>
# open PR -> watch the check run -> partner reviews -> merge

# which model, for what (Section 2 aside)
plan / complex work    -> strongest model (e.g. Opus)
mechanical, well-spec'd -> faster/cheaper model (e.g. Sonnet, Haiku)

# Act II: make Claude yours (Sections 7-9)
CLAUDE.md   -> always read (on the desk) -> the few things always true
a skill     -> read only when relevant  -> "how we build for the church"
  /skills   -> create one; the DESCRIPTION is what makes it trigger
  it missed? -> fix the skill, not just this session (banked for next time)
a routine   -> the loop with nobody at the keyboard
  - no permission prompts, and it ACTS AS YOU  -> scope it tightly
  - it PROPOSES; CI still DECIDES              -> never a merge gate
```

---

## Session Retrospective — Treat the Session Like a Sprint

**Deck:** [Slide 18](slides.html#s29)

Borrowed straight from Agile: a sprint doesn't end when the work ships — it
ends with a **retrospective**, a few minutes where the team looks at *how it
worked*, not just *what got built*. Run each session the same way. Before
anyone leaves, close the room with three questions:

1. **What went wrong?** — where did we get stuck, lose time, or repeat a
   mistake from last session? Name it plainly and without blame; the point is
   to fix the process, not to fault a person.
2. **What should we continue doing?** — what actually worked and is easy to
   drop by accident? Say it out loud so it carries into the next session on
   purpose.
3. **What should we stop doing?** — what cost more than it gave? Retire it
   deliberately instead of carrying it forward out of habit.

**Why this belongs here specifically.** It's the same feedback loop as Section
8, pointed at the *room* instead of a skill. There, a misfiring skill gets
fixed once and the fix is *banked* for everyone from then on. A retro does
that for the session itself: a correction the group agrees on here becomes how
the next session runs, so the process compounds the same way the skills do —
one honest correction at a time. Keep it short (five minutes), keep it
regular, and write the answers down somewhere the group will see them next
time — an evaporated retro improves nothing.

> **Facilitator note.** Keep it blameless and specific. "The lab ran long
> because we debugged setup live" is actionable; "the lab was slow" is not.
> One concrete change per question is plenty — a retro that produces ten fixes
> produces none. This is also worth modelling early: by the time attendees
> pair on real church project tickets (the Gate, Session 19), running a clean
> retro is part of working on a team, not an afterthought.

---

## Homework Before Next Session

**Deck:** [Slide 19](slides.html#s30)

- [ ] Extend the tool built in-session with one more small feature, same PR discipline (branch → Claude → review → PR → CI → merge)
- [ ] Deliberately spot-check one Claude-authored diff for a hallucinated API/method before running it
- [ ] Write one vague prompt and one good prompt for the same small task, and notice the difference in what comes back
- [ ] Find one thing your tool hand-rolls (a control, a bit of layout) and name an existing library that already solves it — note what you'd change if you rebuilt it that way
- [ ] Use the skill you made this session on a real task; when it misfires, tighten its `description` and note what changed (Section 8)

---

## Facilitator Note — This Is Now a Fuller Session

Session 3 has two acts, and together they run past a strict single hour:

- **Act I (Sections 1–6 + Hands-On Lab):** the one-off vibe-coding loop —
  prompt, review, ship through CI. This is the momentum/hook half and can stand
  alone if you're tight on time.
- **Act II (Sections 7–9 + Act II Lab):** making Claude durable — Skills, the
  feedback loop, and Routines, configured live on attendees' machines.

If you're running strictly to 60 minutes, treat these as **Part A / Part B**
across two sittings rather than cramming. Act II is deliberately hands-on
because it needs attendees' own working environment set up — that's why it
lives here (in person, with time) rather than being left to Session 11.

Act II is the *practical* introduction: make a skill, improve it, scope one
routine. **Session 11 is the deep version** — Hooks, Githooks, agentic loops,
building a custom MCP server, and Routines as the payoff once Claude has real
tools to run. Point there explicitly so the two sessions read as a hand-off,
not a repeat.
