# Session 2 — Screenshots

Drop the files in this folder using the exact filenames below. The slides
already reference them; each one shows a dashed `drop in <filename>`
placeholder until the file exists, then swaps to the image automatically.
No markup changes needed.

## Before you capture

- **Switch GitHub to dark mode** — Settings → Appearance → Dark default.
  Light-mode screenshots glow against these slides.
- **Use the sandbox repo, not idmc-gcfsm.** This repository is public;
  real project screenshots leak collaborator names and branch names.
- **Crop tight** to the relevant UI. No browser chrome, no bookmarks bar,
  no OS menu bar.
- **~1400–1600px wide**, PNG, landscape. 2× if your display allows —
  these get projected. Tall screenshots will crowd the slide.

## The files

### `pr-checks-green.png` — slide 14

The **Checks** section of a pull request, `lint-and-test` passing, with
"All checks have passed." Include the green tick and the merge box if it
fits. This is the payoff for the whole first hands-on.

### `merge-button-blocked.png` — slide 17

A pull request blocked by failing required checks. Capture the whole
merge box: the "Some checks were not successful" header, the failing
checks with their **Required** labels, and the button underneath.

**Capture it with auto-merge on, not off.** The instinct is to find a
clean "Merge greyed out" shot, but the version worth teaching is the one
with **Enable auto-merge** showing — because that button is clickable, and
it looks exactly like permission to merge. It isn't: auto-merge tells
GitHub to merge later, once the checks go green. A blocked PR that still
offers a clickable button is the thing people misread, so show it and
explain it. The script for slide 16 has the wording.

A Dependabot PR with red checks makes a good subject — no need to break
anything on purpose.

### `failed-run-log.png` — slide 19

An expanded **failing step** in a workflow run, with the error visible in
the last few lines. Crop so the error is on screen — a wall of setup logs
with the error cut off defeats the "read from the bottom up" lesson.

### `dependabot-pr.png` — slide 21

A real Dependabot pull request: the title with the version bump, the
changelog/release-notes section it generates, and ideally a check running
on it.

### `pages-live.png` — slide 23

The **Pages** settings panel showing "Your site is live at …", or the
Deployments entry in the repo sidebar. Proof that merging shipped
something.

## Optional, not yet wired into the deck

- `actions-run-anatomy.png` — a workflow run page with the job list on the
  left and expanded steps on the right, to sit alongside the vocabulary
  slide. Annotating the three regions (workflow / job / step) would make
  it much stronger.
- `actions-usage.png` — Billing → Actions usage, showing minutes against
  the 2,000 quota, for the free-tier slide.

Say the word and I'll add slides for either.
