# Session: Vibe Coding Your First App (with Claude)

**Status:** [~] In progress — outline drafted, needs full write-up + slides

## Goal

Build a small, working app end-to-end using Claude as a coding partner —
using the safety nets from Sessions 1 and 2 for real, not as theory. This
is the momentum/hook session: the payoff for the fundamentals, not a
reward that comes after them.

## Prerequisites

Session 1 (Git/PR), Session 2 (CI/CD), basic terminal comfort

## The Hook — Why This Is Session 3, Not Session 1

Session 1 gave you history/branches as a safety net. Session 2 gave you an
automated check as a second safety net. Session 3 is where both actually
get used, on purpose: you let Claude make sweeping, fast changes, and the
two things that make that *safe instead of reckless* are already in place
from the last two sessions. Open with that framing before touching a
keyboard — it's the throughline, not a new topic.

**Scope note, deliberately narrow:** the "app" here is intentionally
small and framework-free — a CLI script or a single-file static
page/tool, not a React app. Session 4 owns React/Vite/Next.js properly;
introducing a framework here would make this session about framework
setup friction instead of about the Claude-partnership workflow, which is
the actual point.

## Outline

1. **What "vibe coding" means, and when it's appropriate**
   - Fast, prompt-driven iteration vs. hand-typing every line
   - Good fit: prototypes, scripts, throwaway tools, first drafts
   - Bad fit (or needs extra scrutiny): security-sensitive code, anything
     touching real user data, code you can't easily test/verify
   - Not "no review" — Sessions 1 & 2's discipline still applies, just
     applied to Claude's diffs instead of your own

2. **Setting up a project with Claude's help**
   - Starting from an empty folder vs. an existing repo
   - Writing an initial prompt: describing the *what* and constraints,
     not dictating implementation line-by-line
   - Letting Claude propose a plan/structure before it writes code

3. **Iterating on prompts vs. iterating on code**
   - When to redirect Claude with a better prompt vs. when to just edit
     the file yourself — knowing which is faster
   - Giving Claude feedback on *why* something's wrong, not just "fix it"
   - Small, checkpointed asks beat one giant "build the whole thing" prompt

4. **Reviewing AI-generated code before accepting it**
   - Direct callback to Session 1's diff-review discipline — same skill,
     now applied to a much higher volume of generated code
   - What to actually check: does it do what you asked, does it match
     existing patterns in the repo, anything that looks hallucinated
     (an API/method that doesn't actually exist)
   - Running it locally before trusting it — Claude's confidence isn't
     evidence

5. **Committing, pushing, and letting CI + branch protection do their job**
   - This is the loop closing: Session 1 mechanics + Session 2's required
     check, now exercised on a real PR from today's work
   - Small, frequent commits (the muscle memory from Session 1) even when
     Claude is doing the typing

6. **Common failure modes — set expectations before they hit one**
   - Claude sounding confident about something wrong (hallucinated
     imports, made-up config options)
   - Accepting a big diff without reading it because it "looks right"
   - Prompting vaguely and getting a vague/over-engineered result back

## Agenda (draft — assumes a short discussion + longer hands-on, per
Sessions 1–2's actual pacing)

- [ ] Recap + the hook framing (~5 min): "you have two safety nets now, let's use them"
- [ ] What vibe coding is / isn't, appropriate use (~10 min discussion)
- [ ] Live demo: build the small app from an empty folder, narrating prompts (~15–20 min)
- [ ] Hands-on lab: attendees build their own small tool with Claude (~30–40 min)
- [ ] Wrap-up: PR review pass, tie back to Session 1/2 checks (~5–10 min)

## Hands-On Lab (draft)

Each attendee (or pair) picks — or is assigned — a small, scoped tool to
build with Claude against their sandbox fork, e.g.:
- A CLI script (e.g. a simple file renamer, a word-count tool)
- A single-file HTML/JS page (e.g. a small calculator, a checklist app)

Constraint that matters more than the idea itself: **it must ship as a
real PR**, checked by the CI workflow from Session 2, reviewed by a
partner using Session 1's review habits. The artifact is secondary to
practicing the full loop once, end to end, with Claude doing the typing.

## Handout / Cheat Sheet (TBD)

Likely a "good prompt vs. vague prompt" comparison card, plus a short
"red flags in a Claude diff" checklist — expand once the full session is
written up.

## Homework (draft)

- [ ] Extend the tool built in-session with one more small feature, same PR discipline (branch → Claude → review → PR → CI → merge)
- [ ] Deliberately spot-check one Claude-authored diff for a hallucinated API/method before running it
