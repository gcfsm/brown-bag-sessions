# Session 2 — Speaker Script

The slides hold the shape. This holds the words.

Every slide was cut to what a room can absorb at a glance; the argument
that used to be printed on them lives here. Not a read-aloud — say it in
your own words. The point is that nothing important exists only in your
head on the day.

**Slides not listed** (title, recap, the stack, anatomy of a workflow) are
self-explanatory on screen and need no script.

---

## 4 — "Ten people branch Monday. Everyone merges Friday."

**On screen:** the converging-branches diagram, one line underneath.

> Five people, five branches, Monday morning. Everyone works all week.
> Each branch is fine — it builds, it runs, the person who wrote it is
> happy.
>
> Friday afternoon, everyone merges. And *that* is the first moment
> anybody finds out whether these five sets of changes can coexist.
>
> Notice what that means: the riskiest moment of the week is scheduled for
> the time when everyone is most tired and least willing to start over.

---

## 5 — "The longer you wait to integrate, the more it costs"

**On screen:** four numbered failures, plus a closing line about review.

> **`main` stops being trustworthy.** Nothing checks `main` after a merge.
> So if I ask "does `main` work right now?" — nobody here can answer
> without pulling it down and running it. Every decision downstream
> assumes an answer nobody actually has.
>
> **Cause and effect come apart.** Ten changes land Friday and the build
> goes red. Which one? With CI that's a fact you already have — the run
> that turned red names the commit. Without it, it's an investigation.
> Somebody's afternoon.
>
> **Feedback arrives too late to be cheap.** A bug found a minute after
> you write it costs a minute. The same bug three weeks later costs far
> more — the author has moved on, the context is gone, and someone is
> reading unfamiliar code trying to reconstruct what was meant.
>
> **The team's instinct inverts.** This is the one that does real damage.
> Merging starts to feel dangerous, so people merge less often to avoid
> the mess — which is exactly what makes the next merge bigger. The
> instinct that feels safe is the one making it worse.

**Closing line:**

> And you can't review your way out of this. Not because reviewers are
> careless — because a human reading a diff cannot run the whole test
> suite in their head. That's a category of work people are bad at and
> machines are good at.

---

## 6 — "Continuous Integration: merge early and often, verify every time"

**On screen:** without-CI / with-CI columns, one closing line.

> The name is from the late nineties, out of Extreme Programming, and it's
> almost aggressively literal: integrate continuously. Don't save it up.

**The line that was cut, worth saying in full:**

> This is the missing half of Session 1. Last session you learned that Git
> makes merging cheap — branch, PR, merge, all day. What I didn't say then
> is that cheap merging alone isn't enough at team scale. You also need
> automatic verification on every merge.
>
> Git gives you the *ability* to merge constantly. CI is what makes doing
> so *not reckless*. You need both halves.

---

## 7 — "If `main` always passes, shipping `main` can be automatic"

**On screen:** the definition line, two branch→environment rows, a
pointer to the demo.

**Before the rows:**

> Here's what CI buys beyond a green check. Once every merge is verified,
> you can trust `main` is always in a shippable state. And once *that's*
> true, shipping stops being its own dreaded event — the Friday-night
> deploy, the rollback plan, the person who stays late. It becomes no
> click at all. That's Continuous Delivery, or Deployment, depending how
> far you take it.

**On the rows:**

> A real project points that same mechanism at more than one place. Each
> long-lived branch owns an environment — its own running copy, its own
> database, its own URL.
>
> A PR merged into `develop` deploys to dev. That's where the team pokes
> at it first: real infrastructure, real deploy, nobody outside affected.
> Then `develop` into `main` deploys to prod, and users get it.
>
> Same mechanism, two places. Nothing reaches users that hasn't already
> run somewhere real.

**Handing off:**

> I'll show you this running on idmc-gcfsm — environments, secrets, the
> parts Session 7 covers properly.
>
> What you build later has one rung instead of two: `main` goes live, no
> dev tier. That's deliberate. One environment is enough to feel the
> mechanism; the second is configuration, not a new idea.

---

## 8 — "DevOps is a practice before it's a job title"

**On screen:** a table mapping each ops responsibility to the thing we
actually do for it, and when in the curriculum it lands.

> You've seen a whole pipeline now. Fair question: whose job is this?
>
> The word is DevOps, and it named a way of working before it named a
> role: developers and operations sharing one goal — shipping safely, and
> often — instead of developers tossing releases over a wall and
> operations catching them, then both blaming each other when it broke.
>
> "DevOps engineer" became a job title afterward. Plenty of people in the
> field think that's self-defeating: if a separate DevOps team owns
> delivery, you've rebuilt the wall the idea existed to remove. You'll
> still see it in postings, so know both things.

**On the table — this is the point of the slide:**

> Read the left column and it's the classic ops job. Pipelines,
> environments, secrets and access, monitoring, cost. Twenty years ago
> every one of those meant a machine somebody owned — provision it, patch
> it, configure the web server, manage SSH keys, size it for traffic.
>
> Now read the right column. That is the Firebase and GitHub work we're
> doing across this whole curriculum. Setting up a Firebase project per
> environment *is* environment management. Service accounts and IAM *are*
> access control. Budget alerts *are* capacity planning.
>
> So when we get to Session 7 and spend an hour on Firebase setup, that
> isn't a detour from the real work — that's ops, and you're the one
> doing it.

**The honest caveat, if someone asks:**

> Not everything in Firebase is ops. Data modeling, auth flows, the logic
> inside a Cloud Function — that's application development that happens to
> live in the same console. Security rules sit on the line: they work like
> access control but they're really app authorization written as config.
> The *setup* is ops. What you build on top of it is building.

**Closing:**

> There's no server to provision. The ops work became configuration that
> lives in your repo, reviewed like any other change. That's why it lands
> on developers now — and why on a team our size nobody holds this title.
> You merge the PR, you own what happens next.

---

## 9 — The Claude / vibe-coding thread

**On screen:** one pull quote, nothing else.

**The sentence that was cut:**

> A workflow doesn't get tired. It doesn't skip a step because the code
> looked fine, or because it's 6pm on a Friday. It checks the result the
> same way on the hundredth run as the first.
>
> And that matters more, not less, once Claude is writing diffs. If Claude
> can propose a change and you can merge it in minutes, CI is what stops
> "fast" from becoming "fast and broken."

---

## 10 — "Workflow, trigger, job, step, action, runner"

**On screen:** the six terms and what each one means.

**Name the collision — it trips people up, and GitHub caused it:**

> One warning before we go through these. GitHub named the product
> "Actions," and then named one of the things inside it "an action." Those
> are not the same size at all.
>
> **GitHub Actions**, capital A, is the whole platform — the tab in your
> repo, the minutes you're billed for, the marketplace.
>
> **An action**, lowercase, is one reusable step someone published. Like an
> npm package, but for CI steps.
>
> And the file you write is neither — that's a **workflow**.
>
> So today is mostly about writing workflows. We'll use a few actions
> along the way — `checkout` and `setup-node` on the next slide are two of
> them — but you could write a perfectly good workflow using none at all,
> just shell commands.

---

## 11 — "Build, lint, test"

**On screen:** three verbs, three definitions, one line on the name.

> Three words you'll see in every workflow you write, including the one on
> the next slide.
>
> **Build** — does it compile and bundle at all. **Test** — does it do
> what it's supposed to. Those two are probably intuitive.
>
> **Lint** is the odd one. It's asking: is this written the way the team
> agreed? Not "is it broken" — "is it sloppy." Unused variables,
> inconsistent formatting, a `console.log` you forgot to remove.

**The etymology — worth telling, people remember it:**

> The name is genuinely from the lint on your clothes. The original tool
> was written at Bell Labs in 1978, by a man named Stephen Johnson, to
> catch things in C that the compiler let through silently.
>
> The metaphor is exact: a compiler only cares whether your code *runs*.
> Lint picks off the fuzz — the stuff that's technically legal but
> shouldn't be there. Same as taking a roller to a jacket.
>
> The name stuck, so any tool like this is now "a linter." Ours is ESLint,
> and `npm run lint` is what runs it.

---

## 13 — "From zero to a check on your PR"

**On screen:** the terminal commands, the four-step flow, one line.

**The payoff, said rather than printed:**

> Notice what changed for the reviewer. Before this, if I wanted to know
> whether your PR was broken, I had to pull your branch down and run the
> tests myself. Now the PR tells me before I even open it.
>
> And once the workflow has run on `main` once, you can drop a CI badge in
> your README — a green check anyone can see on the front page of the
> repo, without opening the Actions tab.

---

## 15 — "GitHub Actions free-tier limits"

**On screen:** the limits table, one line, the caching snippet.

**The arithmetic, said out loud:**

> A lint/test job runs about one to three minutes. So 2,000 free minutes a
> month is several hundred runs — genuinely plenty for a project this
> size.
>
> But the ceiling is real, and I want you to know it exists before you hit
> it rather than after. Session 16 comes back to cost properly.
>
> Two things that matter: public repos are unlimited, so if the repo isn't
> sensitive, that decision alone removes the ceiling. And `ubuntu-latest`
> is the cheapest runner — macOS burns ten times the minutes for the same
> job, Windows twice.

---

## 16 — "718 hours of compute"

**On screen:** the Actions usage metrics for a real organisation, one month.

**Lead with the offload. Cost is the follow-up question, not the point:**

> This is a month of Actions usage on an org I work on. Forty-three
> thousand minutes. That's seven hundred and eighteen hours of compute —
> which is a machine building and testing around the clock, for the entire
> month.
>
> And I'm the only developer on it.
>
> None of that ran on my laptop. Nineteen thousand job runs, and not one
> of them made my fan spin or stopped me working while I waited. It ran on
> machines I don't own, in parallel, while I did something else.

**If someone asks what it costs — and they will:**

> Twenty-one dollars a month. My plan includes fifty thousand minutes and
> I used forty-three, so no overage. But notice: that's eighty-six percent
> of what's included, from one person. The ceiling on the previous slide is
> real. I'm just under mine.

**Then defuse it, or they'll think CI is out of reach:**

> Don't read this as "CI is expensive." Read it as what happens when a
> project has been running for years. The workflow you write in twenty
> minutes will use about twenty minutes a month, on the free tier, forever.

---

## 16 — "Making the check mandatory"

**On screen:** five checkbox steps, one closing line.

> One thing about the last item — "require branches to be up to date." That
> is the "merge often" half of this session, enforced automatically. It
> means you can't merge a branch that hasn't caught up with `main`, so
> nobody can quietly sit on a stale branch for three weeks.
>
> Also worth knowing: the status check won't appear in that dropdown until
> the workflow has run at least once. So run it first, then come set this
> up. People get stuck there.

**Closing:**

> And this is the part that matters. The merge is refused until the check
> passes and someone approves. It isn't discipline, it isn't a reminder in
> a group chat, nobody has to remember. GitHub mechanically refuses.

**The trap on the next slide — say this before someone asks:**

> Look carefully, because this confused me too. There *is* a clickable
> button here, and it says "Enable auto-merge." That is not a merge button.
>
> Auto-merge is the opposite: it tells GitHub "merge this for me later,
> once every required check goes green." Click it and nothing happens now.
> The PR just waits.
>
> GitHub only offers auto-merge *because* the merge is blocked. So a button
> you can click is not evidence the protection failed — check whether it
> says "Merge pull request" or "Enable auto-merge." They mean opposite
> things.
>
> The one real exception is a bypass. If you're on a ruleset's bypass list,
> you get a genuine merge button plus a line saying you're allowed to
> bypass. If you don't see that sentence, you don't have it.

---

## 18 — "Reading a failed Actions run"

**On screen:** the workflow on the left, common failures on the right.

> Everyone hits a red X. The skill isn't avoiding it, it's reading it
> without panic.
>
> The one habit worth building: **read from the bottom up.** A failed run
> can be hundreds of lines, and almost all of it is fine. The error is in
> the last few. People scroll from the top, get overwhelmed, and give up
> before reaching the part that tells them what's wrong.
>
> And before you push a fix — reproduce it locally. `npm install`, then
> `npm run lint`, then `npm test`. Same commands the runner ran. Pushing a
> guess and waiting three minutes to find out is a slow way to work.

**On the right column:**

> These four cover most first failures. The second one catches people
> constantly: it works on your machine because the file is *on* your
> machine — you never committed it. The runner starts from a clean clone,
> so it doesn't have it.

---

## 20 — "Dependabot: security alerts vs. routine bumps"

**On screen:** the config, the alert-vs-bump table, one closing line.

**Whose job was this before? Worth asking the room:**

> Mostly nobody's. That's the honest answer. It fell to whoever happened to
> notice — a developer already in that file, a lead doing a cleanup nobody
> scheduled, or a security team forwarding an advisory. There were tools,
> but you had to remember to run them. No ticket, no owner, no deadline.

**The failure mode — this is the point:**

> So dependencies drift. Two years later someone tries to upgrade and every
> package is four majors behind, each with breaking changes, and they
> interact. What should have been fifty one-line diffs is a three-week
> project everyone is afraid to start — so it gets postponed again.
>
> That is slide 4 with different nouns. Batch the work and each unit becomes
> terrifying. Do it weekly and each one is a diff you barely read.

**A real example, if you want one:**

> On Android this is forced on you. Play Store raises the required target
> API level, so the upgrade happens on Google's schedule, not when your team
> has room. And it cascades — the SDK forces Gradle, Gradle forces the
> plugins, the plugins force the libraries. Thirty upgrades at once because
> one was mandatory.

**The honest limit — say this, don't oversell:**

> Dependabot does not fix that. A forced major bump still cascades. What
> changes is what you carry into it: one hard upgrade, instead of one hard
> upgrade plus two years of unrelated rot.

---

## 22 — "Your first deploy"

**On screen:** `deploy.yml`, the Pages setting, the closing line.

> This is GitHub Pages, not Firebase — deliberately. Firebase deploy needs
> a service account secret and project setup, which is real infrastructure
> and belongs in Session 7. Pages needs no account and no secret; it
> deploys straight from the repo you already have.
>
> Merge this and `main` deploys itself to your-username.github.io/repo.

**Deliver the closing line, don't read it.** Let the deploy finish, let
someone see the live URL, then stop and say it slowly:

> You didn't deploy anything. You merged a PR, and the deploy happened
> *to* you. That's the whole idea.

---

## 24 — "Replay the conflict"

**On screen:** five numbered steps, one closing line.

> Same activity as Session 1 — same partner, same conflict, deliberately.
> The only thing that changed is what's watching.
>
> Last time, resolving a conflict was the end of the story. This time,
> merging the resolution kicks off a check *and* a deploy, and the site
> updates while you watch.

**Deliver the closing line, don't read it.** Wait until both the check
and the deploy have fired on screen, then:

> The conflict-resolution skill didn't change since Session 1. Everything
> wrapped around it did. That's what this whole session added.

---

## Related README sections

Participant-facing versions of the same material — for the handout, not
the room:

- `README.md` → "Why CI/CD Exists — Integration Hell"
- `README.md` → §5 "Reading a Failed Actions Run"
- `README.md` → §7 "Your First Deploy — Experiencing CD"
