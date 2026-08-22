# GITCom — Session 4: React on Firebase — and Where Each Choice Deploys

**Status:** [x] Ready

**Goal:** By the end of this session, you can place React, Vite and Next.js in the twenty-year story that produced them, name every layer of the stack we've committed to, treat "Vite or Next.js" as a **deployment decision on Firebase** rather than a matter of taste, put that decision into the prompt you hand Claude, and recognise which of the two paths a project you didn't set up is already on.

**Contents:** [The Seam](#the-seam--what-you-wrote-in-session-3-was-2006) · [A Short History](#1-a-short-history-of-javascript-on-the-web) · [The Altitude](#2-the-altitude-for-today) · [The Stack, Restated](#3-the-stack-restated--we-already-decided-firebase) · [The Vocabulary](#4-the-vocabulary-you-actually-need) · [The Fork in the Road](#5-the-fork-in-the-road--this-is-a-deploy-decision) · [Path A: Vite → Hosting](#6-path-a--vite--firebase-hosting) · [Path B: Next.js → App Hosting](#7-path-b--nextjs--firebase-app-hosting) · [What Next.js Doesn't Replace](#8-what-nextjs-does-not-replace) · [Putting It in the Prompt](#9-putting-the-decision-in-the-prompt) · [Reading an Existing Project](#10-reading-a-project-you-didnt-set-up) · [Hands-On Lab](#hands-on-lab) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

---

## The Seam — What You Wrote in Session 3 Was 2006

**Deck:** [Slide 2](slides.html#s2)

Session 3's tool was a single HTML file on purpose — no framework, no build step, because the point was the Claude-partnership workflow, not tooling. If you extended it in the homework, you probably felt the seam: a second feature meant more `document.getElementById`, more `innerHTML` string-building, and more places where what's on screen could quietly drift out of sync with what your data actually said.

**Here's the thing worth saying out loud: that wasn't a beginner mistake.** That is precisely how professional web development was done, by everyone, for about a decade. You didn't write bad code — you wrote 2006.

Which makes it the right place to start, because everything this session is about is the twenty-year argument the industry had *with that exact pain*. React, Vite, Next.js, and the two different Firebase products they deploy to are all downstream of it. Take the history out and today's decision looks arbitrary. Leave it in and the decision becomes obvious.

---

## 1. A Short History of JavaScript on the Web

**Deck:** [Slides 3–7](slides.html#s3)

Four eras, then the loop closes. **The pattern to point at as you go: each era solves the previous era's pain, and creates the next era's.** Nothing here was fashion. Every one of these was somebody's very reasonable answer to a real problem.

### 1.1 The server rendered everything — JavaScript was garnish

**Deck:** [Slide 3](slides.html#s3)

Through roughly 1996–2008, the server built the entire HTML page for every single request. PHP, ASP, JSP, later Rails: you clicked something, the browser threw the whole page away, asked the server for a new one, and repainted. **Every interaction was a full page reload.**

JavaScript in this world was decoration on top of that: validate a form before submitting, swap an image on hover, open a dropdown. It was not where your application lived.

And it was miserable to write, for a reason that has nothing to do with the language: **every browser did something slightly different.** IE6 against Firefox against Safari meant the same twenty lines needed three variations. That is the specific problem **Prototype.js** (2005, out of the Rails world) and then **jQuery** (2006) existed to solve — one function that worked everywhere, so you stopped writing browser-detection branches. jQuery got enormous not because it was clever but because it made the pain stop.

Then **AJAX** (the term was coined in 2005) let a page fetch data from the server *without* reloading. Gmail and Google Maps were the demos that made everyone stop and stare — a web page that moved and updated like a real application. And that raised the obvious question that ended the era: **if we can update the page without reloading it, why are we reloading it at all?**

**Say this out loud:** what you wrote in Session 3 — reach into the page, set some HTML, hope it matches the data — is this era's style, minus jQuery. You have now personally experienced why the next twenty years happened.

### 1.2 The SPA — the browser takes over

**Deck:** [Slide 4](slides.html#s4)

Around 2010 the answer to that question arrived: the **Single Page Application**. Load one page, once, and then never reload it again. **Backbone.js** (2010) and especially **AngularJS** (2010, from Google) made it a mainstream way to build.

**The role of the server flips.** It stops sending pages and starts sending **data** — JSON. The browser now owns rendering, routing, and application state. AngularJS's famous feature was two-way data binding: change the data, the screen updates itself, no `getElementById` anywhere. If that sounds like the fix for your Session 3 pain, that's because it was.

**And it created two new problems, both of which are still live decisions today:**

1. **Nothing shows until a large bundle of JavaScript downloads and runs.** On a slow phone, a blank screen for a while.
2. **Search engines got an empty page.** A crawler asked for the URL and received a near-empty shell — the real content only existed after JavaScript ran, and in 2010 Google mostly didn't run it.

**That second problem still shapes the decision — but don't overstate it, because it's the one an attendee may push back on.** Google fixed most of it: it now renders JavaScript on a second pass, so a client-side app *does* get indexed. What it doesn't get is speed or certainty — that pass is queued behind the initial crawl and can land days later, anything revealed only by a click or scroll isn't seen at all, and non-Google crawlers (Bing, social link previews, AI crawlers) are further behind. So the modern form of the problem is **delayed and less certain**, not invisible. Section 8 has the full correction; it's still the reason a church's *public* site and its *internal* dashboard get different answers.

### 1.3 Node.js — JavaScript escapes the browser

**Deck:** [Slide 5](slides.html#s5)

In 2009 Ryan Dahl took V8 — Chrome's JavaScript engine — out of the browser and wrapped it in a runtime that could read files, listen on ports, and talk to databases. **Node.js.** JavaScript was suddenly a server language.

Two consequences, and both are in your terminal already:

- **One language on both sides.** The same person could write the browser code and the server code. That's the moment "full-stack JavaScript developer" became a real job title.
- **`npm` (2010) became the way code gets shared** — and then the way *tooling* gets built. This is the honest answer to a question beginners are right to ask: why does a front-end project need `npm install` at all, when the browser is the thing running the code? Because the *tools* — the build step, the dev server, the linter — are Node programs. **Vite runs on Node. So does Next.js. So does the CI job you built in Session 2.**

Node didn't change what the browser does. It changed what the industry could build to help you write for the browser — and it quietly set up the era where the two sides could merge again.

### 1.4 React and Vue — the component era

**Deck:** [Slide 6](slides.html#s6)

**React** (Facebook, 2013) and **Vue** (2014) changed the unit of work. Not the page. Not the DOM node. **The component** — one self-contained piece of screen that owns its own patch.

And with it, the shift that actually matters: **you stop issuing instructions and start making a declaration.** The old way was imperative — *find this element, change its text, hide that one.* The new way is declarative: **describe what the screen should look like for a given state, and let the library work out what to change.** The drift you felt in Session 3 — screen saying one thing, data saying another — becomes structurally hard, because there is no longer a second copy of the truth to drift from.

This is where the industry has stayed for over a decade, which is why we teach React and not the thing after it. It's not a trend; it's the settled answer.

### 1.5 The loop closes — server rendering comes back

**Deck:** [Slide 7](slides.html#s7)

Now put the last two eras together. You have JavaScript that runs on a server (era 3) and components that describe a UI (era 4). So you can run the components **on the server**, send the finished HTML to the browser, and then let it become a live app once the JavaScript arrives.

That's **server-side rendering** — and look closely at what it is. **It's era 1's answer, rebuilt with era 4's tools.** The server sends a real, complete page again, which fixes exactly the two problems the SPA created: something is on screen immediately, and a crawler gets actual content.

**Next.js** (2016) is that idea packaged. **Vite** (2020) is the modern, fast tooling for the SPA path — the era-2 lineage, done well.

**Say this out loud, because it's the whole point of the history:**

> The wheel came back around. Vite is the descendant of the SPA era. Next.js is the descendant of the server-rendering era. **Neither one is out of date — they are two different answers to a twenty-year-old argument, and which one is right depends on whether a stranger needs to find your page on Google.**

**And that is why they deploy to two different Firebase products.** A descendant of "the browser does everything" needs somewhere to put files. A descendant of "the server renders the page" needs a server that keeps running. The rest of this session is just that sentence, made concrete.

---

## 2. The Altitude for Today

**Deck:** [Slide 8](slides.html#s8)

**There is deliberately no code on these slides.** Session 3 settled how we work: you state the *what* and the *constraints*, Claude writes it, you check whether it answered the right question. Handing you JSX to memorise two weeks later would contradict that.

What you can't delegate is the decision that comes *before* the prompt. Claude will happily build you either a Vite app or a Next.js app — and it will not stop to mention that those two answers deploy to different Firebase products, on different billing plans, with different amounts of work the first time you need something to run on a server. That call is yours, it's made on day one, and it's expensive to reverse.

**Sessions 1 and 2 stay hand-typed, no-AI-shortcuts.** That boundary doesn't move.

---

## 3. The Stack, Restated — We Already Decided Firebase

**Deck:** [Slide 9](slides.html#s9)

Worth saying plainly, because everything after this session assumes it and it's easy to forget it was ever a choice:

| Layer | What we use | Where it's taught |
|---|---|---|
| UI library | **React** | this session (vocabulary only) |
| Build tool / framework | **Vite** *or* **Next.js** | this session — the decision |
| Database | **Firestore** | Session 5 (modeling), Session 6 (using it) |
| Login | **Firebase Auth** | Session 6 |
| Files & uploads | **Firebase Storage** | Session 7 |
| Server-side code | **Cloud Functions** | Session 7 |
| Hosting | **Firebase Hosting** *or* **Firebase App Hosting** | this session — the decision |
| CI | **GitHub Actions** | Session 2 (already yours) |

**Say this out loud:** Firebase is not one product, it's a shelf of them, and we've committed to that shelf. The practical consequence is that "which framework" is never a standalone question here — it's the question of *which Firebase deployment product you're signing up for*, because each framework lands on a different one.

Committing to a platform is a real trade: a lot of infrastructure a small church team doesn't have to run, in exchange for a stack that's genuinely harder to leave later. We made that trade knowingly. Being clear-eyed about it is part of being able to work in it.

---

## 4. The Vocabulary You Actually Need

**Deck:** [Slide 10](slides.html#s10)

Four words. You need them so your prompt lands and so you can say something useful about what comes back — not so you can type them.

- **Component** — one self-contained piece of the screen that owns its own patch: a volunteer card, a schedule row, a sign-up form. Pages are built by composing them.
- **Props** — data handed *down into* a component from whatever contains it. Read-only from the inside.
- **State** — data a component owns itself, that changes over time. When it changes, that piece of the screen updates to match.
- **Route** — a URL that renders a particular screen.

**The one judgement call worth having an opinion about: where state lives.** If two components both need to know something, it can't be owned privately by either one — it has to live in whatever contains them both, and be passed down. That's the most common structural mistake in generated React, and it's visible without reading a line of syntax. "Both cards need to know the total, so that count shouldn't live inside a card" is a complete, correct review comment.

**Say this out loud:** that sentence is what this section is for. You're not learning React to write it — you're learning enough of it to say something like that to Claude and be right.

---

## 5. The Fork in the Road — This Is a Deploy Decision

**Deck:** [Slides 11–12](slides.html#s11)

The usual framing is "Vite is simpler, Next.js is fuller." True, and useless, because it doesn't tell you what you're committing to. After the history, you can say it properly — **these are two different eras' answers, and on Firebase they land in two different places:**

| | **Vite** (SPA lineage) | **Next.js** (server-rendering lineage) |
|---|---|---|
| What the build produces | Static files — HTML, JS, CSS in a `dist/` folder | A running server application |
| Firebase product | **Firebase Hosting** | **Firebase App Hosting** |
| What serves it | A CDN. No server of yours is running. | A container on Cloud Run, behind a CDN |
| Billing plan | Works on **Spark** (the free plan) | Requires **Blaze** (pay-as-you-go) |
| Routing | Add a library (`react-router`) and wire routes up | File-based — the folder structure *is* the URL structure |
| Search engines | Indexed, but on a delayed second pass — and weaker outside Google | Content is in the first response — nothing to wait for |
| Server-side code | Needs a **separate Cloud Function**, deployed separately | **Built in** — API routes ship in the same app, same deploy |

**The short version:** Vite gives you a folder of files a CDN can hand out. Next.js gives you an application that has to keep running somewhere. **Every row in that table follows from that one difference** — and that difference is 1.2 versus 1.5 above.

**Which to pick, in church terms:**

- **Internal tool, volunteers log in, nobody needs to find it on Google** — a rostering dashboard, an attendance tracker, an admin panel. **Vite → Firebase Hosting.** Login-gated content has no SEO story to lose, so era 2's weakness costs you nothing — and this path is free at our scale.
- **Public-facing site people should find by searching** — the idmc-gcfsm conference site, a ministry landing page, anything with real distinct pages you'd want indexed. **Next.js → App Hosting.** This is exactly the problem the wheel came back around to solve.

**Make this call before the first prompt.** Reversing it later isn't a rename — it's a rebuild of the app's structure *and* a migration between hosting products, which drags in DNS, config, and your CI along with it. This is the cheapest decision in the whole project to get right and one of the most expensive to change.

---

## 6. Path A — Vite → Firebase Hosting

**Deck:** [Slide 13](slides.html#s13)

Vite builds your React app into a folder of plain static files. Firebase Hosting puts that folder on a CDN and serves it. That's the whole model, and its simplicity is the feature.

**What it means in practice:**

- **It runs on the Spark plan** — no credit card. The no-cost allowance is 10 GB of storage and 10 GB of transfer per month, which a church-scale internal tool will not come close to. The caps are hard rather than billable: exceed storage and further deploys are blocked; exceed transfer and the site is disabled until the next billing month. You get a wall, not a bill.
- **Deploys happen when you trigger them** — from the CLI, or from a GitHub Actions workflow like the one you built in Session 2. Session 7 wires that up properly.
- **There is no server of yours anywhere.** Nothing in this app can hold a secret, because everything shipped to the browser can be read by anyone with dev tools open.

**"Client-only" is not "backend-less" — this is the part people get wrong.** A Vite app on Firebase still has a real backend: it talks to Firestore and Auth directly from the browser, and **Firestore security rules** decide who's allowed to read or write what. That's a genuine server-side permission check, just not one you wrote in a function. Sessions 5 and 6 teach that; Session 9 is where the rules get serious.

**When you'd need a Cloud Function anyway** — the work has to happen somewhere the user can't see or tamper with:

- It uses a secret — an email-service API key, a payments key, any third-party credential
- It needs admin privileges that ordinary users' security rules deliberately forbid
- It's a webhook a third party calls, or a scheduled job that runs with nobody there

That's a second, separately deployed thing next to your site. Perfectly normal, and Session 7 covers it. Just know that on this path it's an *addition*, not something that comes in the box.

---

## 7. Path B — Next.js → Firebase App Hosting

**Deck:** [Slide 14](slides.html#s14)

Next.js doesn't produce a folder of files to hand out — it produces an application that runs, renders pages on request, and can answer API calls. That needs somewhere to run, and on Firebase that place is **App Hosting**: a purpose-built product for exactly this, with Next.js as one of its two first-class frameworks.

**What it means in practice:**

- **Deployment is git-triggered.** You connect a repository and nominate a live branch. Push to it, and a build kicks off and rolls out automatically — no deploy command, no manual step. Yes, that means merging a PR ships to production; Session 2's branch protection and required checks are the thing standing between "merged" and "broken in public", which is precisely why that session came first. And "production" is a deliberate word: a real project keeps a **separate dev Firebase project** wired to a dev branch, so a push you're unsure about lands there, not on the live church site — Session 7 covers running dev and prod as two separate projects.
- **Underneath, it's Google Cloud, unhidden.** Cloud Build builds a container, Cloud Run runs it, Cloud CDN caches in front of it. Worth knowing because when something breaks, the logs you need are Cloud Run's, and the bill itemises those services by name.
- **It requires the Blaze plan.** That means billing enabled and a card on file. There are real no-cost allowances on Blaze — roughly 10 GiB/month of outgoing traffic, 2 million Cloud Run requests, and 2,500 Cloud Build minutes — and at church traffic you will very likely sit inside them and pay nothing. But nothing *stops* at the free line the way Spark's caps do: past it, it's a bill. Session 16 is the whole session on watching that.
- **Configuration lives in `apphosting.yaml`.** Environment variables, references to secrets in Secret Manager, and how big the container is allowed to get. You don't need to write one today — you need to recognise the filename as "this is where the deploy is configured" when you see it in a repo.

**The thing you're actually buying: the backend comes with it.** A Next.js app can have API routes — server-side endpoints that live in the same codebase and deploy in the same push. For "the browser must not see this key" work, that's a Cloud Function you don't have to create, deploy, or maintain as a separate moving part.

---

## 8. What Next.js Does *Not* Replace

**Deck:** [Slide 15](slides.html#s15)

Three honest corrections, so nobody leaves with a rule that's too clean:

**1. "Next.js means no Cloud Functions" is false.** It removes one kind: the endpoint *you call* — the client asks, the server answers. It does nothing about the kind that fires *on its own* when something happens: a document was written to Firestore, a file landed in Storage, a new user signed up, or it's 2am and the nightly summary is due. Nobody calls those. There is no request. An API route can't be that, on any platform, because an API route only exists while someone is asking it something. If your app needs that behaviour, it needs Cloud Functions regardless of framework. Session 7 breaks down the trigger types properly.

**2. Blaze doesn't mean expensive.** It means metered instead of capped. Spark says "you can't go past this line"; Blaze says "past this line, it costs." For a church, both are usually free in practice — the real difference is which failure you'd rather have: a site that switches off, or an invoice nobody was watching for. Choose deliberately, and set a budget alert either way.

**3. "Google can't see a React app" is out of date — and someone in the room may know it.** That was era two's problem, and Google largely fixed it. Googlebot now renders JavaScript in a **second pass**: it takes the HTML first, then queues the page for a headless Chromium render that executes your JS and indexes what appears. Client-side apps do get indexed.

What you don't get is speed or certainty:

- **The render pass is queued** behind the initial crawl — hours, sometimes days later, and subject to crawl budget.
- **Anything that only appears after user interaction** — a click, a hover, a scroll — is never seen, because nobody interacts on Googlebot's behalf.
- **Other crawlers are behind Google**, and there are more of them that matter now: Bing, the bots that generate link previews when someone shares your URL in a group chat, and AI crawlers.

So the honest 2026 statement is **"delayed and less certain," not "invisible."** For an internal dashboard that changes nothing. For a conference page with a date on it that people will share in group chats, "probably indexed, eventually" is still the wrong answer — which is why the recommendation in Section 5 doesn't change.

---

## 9. Putting the Decision in the Prompt

**Deck:** [Slide 16](slides.html#s16)

Session 3's rule was: state the *what* and the *constraints*, leave the *how* to Claude. Everything above is now a constraint — and one Claude cannot infer, because from the inside both answers look correct.

```
Weak:
"Build me a React app for volunteer sign-ups."

Strong:
"React + Vite, deploying to Firebase Hosting as a static build. Data
in Firestore, read from the client and guarded by security rules —
no server-side code, no Cloud Functions, and nothing that needs a
secret at runtime. Volunteers sign in with Firebase Auth."
```

The weak prompt gets you *something*. It might be Next.js. It might assume an API route, which means assuming App Hosting, which means assuming Blaze — none of which you asked for, and none of which will be announced. The strong prompt is one sentence longer and closes every one of those gaps.

**Say this out loud, the same way you did in Session 3.** Look at what writing that prompt required: knowing that a Vite build is static, that static implies Hosting, that Hosting implies no server of your own, and that "no server of my own" is exactly why the security rules matter. Four sentences of technical knowledge — and Claude still wrote all the code. That's the shape of this whole track. The knowledge doesn't stop mattering; it moves from your fingers to your judgement.

**Then check the answer against the decision** — no diff-reading required. Did it produce a static build, or an app expecting to run? Is there an API route in there you didn't ask for? Does the config file that showed up match the path you chose? "You gave me API routes, but we're deploying static to Firebase Hosting — no server will exist to run those" is a review comment made entirely at this session's altitude.

---

## 10. Reading a Project You Didn't Set Up

**Deck:** [Slide 17](slides.html#s17)

Most projects you touch will already have made this decision — including older ones still on **Create React App**, often with **Craco** wrapped around it. CRA is the previous generation of what Vite does: same era-2 lineage, same static output for Hosting, just slower and with a different command to start it. Now that you have the history, an unfamiliar tool is placeable rather than alarming — it's someone's answer from a particular year.

**Recognition, not mastery.** Three questions answer it, and Claude will answer all three at once if you open the repo and ask:

> "What is this project — Vite, Next.js, or CRA? Where does it deploy, and does it have any server-side code?"

What you're listening for: **which framework**, **which Firebase product**, and **whether there's a server side**. Those three facts tell you what you can safely propose. Asking for an API route in a project that deploys as a static site isn't a small ask — it's a hosting migration, and now you know that before you suggest it rather than after.

**One tutorial trap worth naming:** you'll find guides deploying Next.js to Firebase *Hosting* rather than App Hosting, using an older framework integration that put the server side into a Cloud Function behind Hosting. It works, and it's not what we're doing. App Hosting is the purpose-built path — don't blend the two sets of instructions.

---

## Hands-On Lab

**Deck:** [Slide 18](slides.html#s18)

**No code in part 1.** This lab is the decision, then the prompt, then checking the answer.

### Part 1 — Call it, in pairs (15 min)

For each, pick **Vite → Hosting** or **Next.js → App Hosting**, and say in one sentence what decided it. Then say whether it needs a Cloud Function *on top* of that choice.

1. A volunteer rostering dashboard. Thirty leaders sign in; nobody else should ever see it.
2. The public conference site — schedule, speakers, venue. People find it by Googling the conference name.
3. A public registration form that emails a confirmation, using a third-party mail service's API key.
4. An internal attendance tracker that also posts a summary to the leaders' group every Sunday at 9pm.

Scenario 3 is the interesting one: **either** path can do it, but the cost differs — on Vite it's a Cloud Function you add, on Next.js it's an API route you already have. Scenario 4 needs a scheduled function no matter what you picked, because nobody is there to call it.

### Part 2 — Prompt it and check it (25 min)

Take **scenario 1**. Write the prompt as a pair, with the framework and the deploy target stated explicitly — Section 9's "Strong" prompt is your template, adapt it. Then let Claude scaffold it, and check the result against your decision:

- Is it Vite, and does building it produce a static folder?
- Is there anything in there that assumes a server you don't have?
- Ask Claude directly: *"where does this deploy, and does any of it need a server?"* — then judge whether that answer matches what you asked for.

**Ship it the usual way:** branch → Claude writes → you review → PR → CI green → partner approves → merge. The artifact is small; the loop is the point, same as Session 3.

**Don't deploy it today.** You have decided *where* it goes; actually putting it there is Session 7, after Firestore and Auth exist in Session 6 to put in it.

---

## Quick Reference Card (keep this open while working)

**Deck:** none — reference material

```
THE HISTORY, IN ONE BLOCK

  ~1996-2008  server renders every page; JS is garnish
              (Prototype '05, jQuery '06 — fix the browsers)
              AJAX: update without reloading. Why reload at all?
  ~2010       SPA. AngularJS/Backbone. Server sends JSON, not pages.
              New problems: slow first paint, invisible to crawlers.
   2009       Node.js. JS on the server. npm '10.
              -> this is why front-end projects run `npm install`
   2013/14    React & Vue. The component. Declarative, not imperative.
   2016       Next.js: render components ON the server.
              = era 1's answer, rebuilt with era 4's tools.

  Vite    = the SPA lineage, modern tooling (2020)
  Next.js = the server-rendering lineage
  Neither is out of date. They answer different questions.

THE DECISION

Vite            -> static files -> Firebase HOSTING
                   Spark (free) plan OK. CDN only, no server of yours.
                   Server-side work = a separate Cloud Function.
                   Best for: internal, login-gated, no SEO needed.

Next.js         -> a running app -> Firebase APP HOSTING
                   Blaze (billing) required. Cloud Run + Cloud CDN.
                   Git-triggered deploy: push to the live branch = ship.
                   API routes built in. File-based routing. Crawlable.
                   Best for: public, needs to be found on Google.

STILL NEEDS A CLOUD FUNCTION ON EITHER PATH
  reacting to a data change (Firestore/Storage/Auth event)
  scheduled jobs (nightly, weekly)
  -> nobody "calls" these, so an API route cannot be one

VOCABULARY (say these; don't type them)
  component -> one self-contained piece of the screen
  props     -> passed down in, read-only
  state     -> owned here, changes over time
  route     -> a URL that renders a screen
  rule of thumb: if two components need it, it can't live inside either

PUT IT IN THE PROMPT
  "React + Vite, static build, deploying to Firebase Hosting.
   Firestore from the client with security rules. No server-side
   code, no Cloud Functions."

READING AN EXISTING PROJECT — ask Claude
  "What is this project - Vite, Next.js or CRA? Where does it deploy,
   and does it have any server-side code?"
```

---

## Homework Before Next Session

**Deck:** [Slide 19](slides.html#s19)

- [ ] Open a real project — idmc-gcfsm, a teammate's, or your own — and work out which path it's on: framework, Firebase product, server-side code or not. Ask Claude if you're unsure; the goal is the answer, not the archaeology.
- [ ] Write the one-paragraph decision for a tool your ministry actually wants: which path, and the one sentence of why. Bring it to Session 5 — some of these become real projects later in the track.
- [ ] Sanity-check one of your Session 3 prompts: if you handed it to Claude today with no other context, could it tell which hosting path you meant? If not, rewrite it so it could.

---

## Facilitator Note — Where the History Is Simplified

The four-era story is a teaching device, and it's a good one, but it's tidier than what happened. **You don't need to teach these caveats — you need to have them ready**, because the room may include someone who lived through this and will (rightly) push back. Conceding the point accurately is better than defending a clean story.

**1. Era one never ended.** Server-rendered pages remained the majority of the web through every era that followed, and still are — WordPress alone is a large share of all sites. The eras describe where the *frontier* moved and where the argument was loudest, not what everyone was doing. This actually makes the closing point stronger rather than weaker: server rendering didn't "come back" so much as the frontier came back around to something that never left, and returned with better tools.

**2. The eras overlap, and one of them is out of order.** Node.js (2009) predates AngularJS (October 2010) — era three technically starts before era two peaks. jQuery stayed dominant right through the SPA years and is still on a very large share of live sites today. It's a sequence of *ideas*, each answering the previous one's pain; it is not a clean chronology, and the numbering is for narrative, not history.

**3. AngularJS didn't invent the SPA.** Gmail (2004) and Google Maps (2005) were single-page applications years before there was a framework category or a name for it. Backbone.js (2010) landed alongside AngularJS rather than after it. Angular 2 (2016) was a full rewrite and is a different framework from AngularJS despite the name — worth knowing if someone says "we use Angular."

**4. Next.js didn't invent bringing rendering back to the server.** "Isomorphic" or "universal" JavaScript was an active idea around 2014–15 — React shipped server rendering, and several projects tried to package it. Next.js (2016) is the one that made it pleasant enough to become the default. "Packaged it" is the accurate verb, and it's the one the notes use.

**5. Vite is not only for SPAs, and Next.js is not only server-rendered.** Vite supports server rendering, and Next.js can export a fully static site. The clean "Vite = era two, Next.js = era one" mapping is a simplification chosen because it makes the Firebase deployment consequence obvious — which is the actual thing being taught. If someone raises it, the honest answer is: those are both true, and neither changes which Firebase product each one lands on by default, which is what we're deciding today.

**6. jQuery was more than a browser-compatibility patch.** It also gave the era its ergonomics — chainable DOM selection, straightforward AJAX, an enormous plugin ecosystem. The cross-browser story is the clearest reason it *spread*, which is why the notes lead with it, but it isn't the whole reason it was loved.
