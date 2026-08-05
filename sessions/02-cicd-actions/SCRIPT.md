# Session 2 — Speaker Script

Talk track for the slides that carry more argument than fits on screen.
The slides hold the shape; this holds the words. Covers slides 5, 7, and 8
— extend as the rest of the deck gets thinned.

Not a read-aloud. Say it in your own words; the point is that nothing
important lives only in your head on the day.

---

## Slide 5 — "The longer you wait to integrate, the more it costs"

**On screen:** four numbered failures, one line each, plus a closing line
about review.

**Say:**

> Take these one at a time, because they compound.
>
> **`main` stops being trustworthy.** Without CI, nothing checks `main`
> after a merge. So if I ask "does `main` work right now?" — nobody in
> this room can answer without pulling it down and running it by hand.
> That's not a small gap. Every decision you make downstream assumes an
> answer nobody actually has.
>
> **Cause and effect come apart.** Ten changes land Friday afternoon and
> the build goes red. Which one did it? With CI that's a fact you already
> have — the run that turned red names the commit. Without it, that's an
> investigation. Somebody's afternoon.
>
> **Feedback arrives too late to be cheap.** A bug found a minute after
> you write it costs you a minute. The same bug found three weeks later
> costs a great deal more — the author has moved on, the context is gone,
> and now someone is reading unfamiliar code trying to reconstruct what
> was meant.
>
> **The team's instinct inverts.** This is the one that does real damage.
> Merging starts to feel dangerous, so people merge less often to avoid
> the mess. But merging less often is exactly what makes the next merge
> bigger, and the one after that worse. The instinct that feels safe is
> the one making it worse.

**Then the closing line:**

> And you can't review your way out of this. I'm not saying reviewers are
> careless — I'm saying a human reading a diff cannot run the whole test
> suite in their head. That's not a skill gap, it's a category of work
> people are bad at and machines are good at.

---

## Slide 7 — "If `main` always passes, shipping `main` can be automatic"

**On screen:** the definition line, the two branch→environment rows, and
a pointer to the live demo.

**Say, before the rows:**

> Here's what CI buys you beyond a green check. Once every merge is
> verified, you can trust that `main` is always in a shippable state. And
> once that's true, shipping stops being its own separate dreaded event
> — the Friday-night deploy, the rollback plan, the person who stays
> late. It becomes no click at all. That's Continuous Delivery, or
> Deployment, depending on how far you take it.

**On the rows:**

> A real project points that same mechanism at more than one place. Each
> long-lived branch owns an environment — its own running copy of the
> app, its own database, its own URL.
>
> A PR merged into `develop` deploys to dev. That's where the team pokes
> at it first — real infrastructure, real deploy, nobody outside affected.
> Then `develop` merged into `main` deploys to prod, and users get it.
>
> Same mechanism, pointed at two places. The point is that nothing
> reaches users that hasn't already run somewhere real.

**Handing off to the demo:**

> I'm going to show you this running on idmc-gcfsm — the environments,
> the secrets, the parts Session 7 covers properly.
>
> What you build later today has one rung instead of two: `main` goes
> live, no dev tier. That's deliberate. One environment is enough to feel
> the mechanism, and the second one is configuration, not a new idea.

---

## Slide 8 — "DevOps is a practice before it's a job title"

**On screen:** two columns — the work, and what Firebase changes — plus
one closing line.

**Say:**

> You've now seen a whole pipeline. Fair question: whose job is this?
>
> The word you'll hear is DevOps, and it's worth knowing it named a way
> of working before it named a role. The idea was developers and
> operations sharing one goal — shipping safely, and often — instead of
> developers tossing releases over a wall and operations catching them
> and blaming each other when it broke.
>
> "DevOps engineer" became a job title afterward. Plenty of people in the
> field think that's self-defeating: if a separate DevOps team owns
> delivery, you've rebuilt the wall the whole idea existed to remove. You
> will still see it in job postings, so know both things.

**On the left column:**

> Whatever you call the person, this is the work: the pipeline,
> environments kept apart, secrets and who's allowed to deploy, and
> monitoring and rollback — noticing when something's wrong and being
> able to undo it.

**On the right column — the correction worth making explicitly:**

> Now, classically a lot of that meant servers. Provision a machine,
> patch it, configure the web server, manage SSH keys, size it for
> traffic.
>
> On Firebase there is no server. Nothing to provision, nothing to patch,
> nothing to SSH into. But the work didn't disappear — it changed shape.
> Firewall rules became Firestore security rules. `sudo` became IAM and
> service accounts. A staging server became a second Firebase project.

**Closing:**

> So the ops work became configuration that lives in your repo, reviewed
> like any other change. And that's exactly why it lands on developers
> now — and why on a team our size nobody holds this title. You merge the
> PR, you own what happens next.
>
> Session 7 sets the Firebase side up properly. Session 15 is monitoring.

---

## Related README sections

Participant-facing versions of the same material, for the handout rather
than the room:

- `README.md` → "Why CI/CD Exists — Integration Hell"
- `README.md` → §7 "Your First Deploy — Experiencing CD"
