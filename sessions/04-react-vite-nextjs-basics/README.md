# GITCom — Session 4: React / Vite / Next.js Basics

**Status:** [x] Ready

**Goal:** By the end of this session, you can explain a component in terms of props and state, recognize which tool a React project uses well enough to run it (even one you didn't set up), and know when a project needs Next.js instead of Vite.

**Contents:** [Why This Session Exists](#why-this-session-exists--what-breaks-as-vanilla-grows) · [Component Basics](#1-component-basics--props-and-state) · [Vite vs. Next.js](#2-vite-vs-nextjs--when-to-use-which) · [Dev Server & Hot Reload](#3-dev-server-hot-reload--functional-literacy-not-mastery) · [If the Project Uses Something Else](#4-if-the-project-already-uses-something-else) · [Routing Fundamentals](#5-routing-fundamentals) · [Hands-On Lab](#hands-on-lab) · [Quick Reference](#quick-reference-card-keep-this-open-while-working) · [Homework](#homework-before-next-session)

---

## Why This Session Exists — What Breaks as Vanilla Grows

**Deck:** [Slides 2–3](slides.html#s2)

Session 3's tool was intentionally a single HTML file — no framework, no build step, because the point was the Claude-partnership workflow, not tooling. But if you extended it in the homework, you may have already felt the seam: adding a second feature means more manual DOM work (`document.getElementById`, more `innerHTML` string-building), and more places where what's on screen can drift out of sync with your actual data.

That's the specific problem React solves. Instead of manually pushing DOM updates every time data changes, you describe what the UI should look like *for a given state*, and React handles making the screen match it. This session is the introductory version of that mental model — just enough to work with it, and to work with Claude on it.

**Scope note, same spirit as Session 3:** you'll mostly vibe-code the actual implementation from here on. This session is deliberately light on build-tool internals — you don't need to understand Vite's or Webpack's internals to use either well, the same way you didn't need to understand V8 to write JavaScript in Session 3. What you need is **functional recognition**: what command runs this, what file configures it, what "this looks different from what I expected" should make you stop and ask. That's a different, thinner bar than mastery — and it's a deliberate choice, not a shortcut. (Sessions 1 and 2 stay hand-typed, no-AI-shortcuts, on purpose — that boundary doesn't move.)

---

## 1. Component Basics — Props and State

**Deck:** [Slides 4–5](slides.html#s4)

A **component** is a function that returns UI. That's it — the rest is two ways data flows through it:

- **Props** — data passed *in* from a parent. Read-only from the component's side; if it needs to change, the parent changes it and passes a new value down.
- **State** — data a component owns itself. When state changes, the component re-renders to match it.

```jsx
function VolunteerCard({ name, role }) {   // props: passed in, read-only
  const [signedUp, setSignedUp] = useState(false);   // state: owned here

  return (
    <div>
      <h3>{name} — {role}</h3>
      <button onClick={() => setSignedUp(true)}>
        {signedUp ? "You're in!" : "Sign up"}
      </button>
    </div>
  );
}
```

`name` and `role` come from whoever renders `<VolunteerCard>` — this component never changes them itself. `signedUp` is local — clicking the button updates it, and React re-renders just this card to match.

**The rule of thumb:** if a parent needs to know about it or control it, it's a prop. If it's private to this piece of UI and changes over time, it's state.

---

## 2. Vite vs. Next.js — When to Use Which

**Deck:** [Slide 6](slides.html#s6)

| | Vite | Next.js |
|---|---|---|
| What it is | A fast dev server + build tool for a client-side app | A full framework — routing, server rendering, and API routes built in |
| Use when | A simple client-only app — no SEO concerns, no need to render on the server | You need real multi-page routing, content that search engines should crawl, or backend API routes in the same project |
| Church example | An internal admin tool or dashboard only logged-in volunteers ever see | A public-facing site like idmc-gcfsm's conference site — needs to be fast and crawlable for visitors, has real distinct pages |

**Neither is "better" — they answer different questions.** Vite asks "how do I run and bundle a React app fast." Next.js asks "how do I build a whole multi-page site, including the parts that aren't just client-side JavaScript." A project needing routing, SEO, or a backend will reach for Next.js from the start; a small internal tool usually doesn't need that weight.

---

## 3. Dev Server, Hot Reload — Functional Literacy, Not Mastery

**Deck:** [Slide 7](slides.html#s7)

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev     # starts a local dev server, prints a localhost URL
```

Open the printed URL. Edit a component, save the file — the browser updates **without a full page reload**, usually keeping your app's current state (a form's contents, a toggle's position). This is **Hot Module Replacement** (Vite) or **Fast Refresh** (Next.js/CRA) — different names, same idea: the dev server watches your files and pushes just the changed piece into the running page.

**What to actually know:** `npm run dev` starts it, the terminal tells you the port, and saving a file is supposed to update the browser without you refreshing. If it *doesn't* update, that's your signal something's actually wrong — not something to puzzle through alone, ask Claude what broke.

---

## 4. If the Project Already Uses Something Else

**Deck:** [Slide 8](slides.html#s8)

Not every React project you touch will be a fresh Vite app — plenty of real, older projects (including some you may end up maintaining) use **Create React App**, often wrapped with **Craco** (a thin layer that lets you override CRA's build config without fully "ejecting" it).

**Recognition, not mastery** — check `package.json`'s `scripts`:

```json
"scripts": {
  "start": "craco start",   // <- CRA + Craco. "npm start", not "npm run dev"
  "build": "craco build"
}
```

Same job (dev server, hot reload, production build), different tool, different command name (`npm start` instead of `npm run dev`). You don't need to understand *why* a project chose Craco over Vite to work in it — you need to notice the script name is different and use the right one. If something in the build genuinely looks broken (not just "unfamiliar"), that's a real question for Claude, not an expectation that you already know Craco's internals.

---

## 5. Routing Fundamentals

**Deck:** [Slide 9](slides.html#s9)

**Client-side routing** means the URL changes and a different component renders — without a full page reload, unlike clicking a plain `<a href>` link to a different server-rendered page.

- **Vite (client-only app):** routing isn't built in — you add a library (commonly `react-router`) and wire up routes yourself: this path renders that component.
- **Next.js:** routing is **file-based** — the folder structure under `app/` (or `pages/`) *is* the URL structure. A file at `app/schedule/page.jsx` is automatically reachable at `/schedule`, no router library, no manual wiring.

Same underlying idea (URL → component), different amount of setup. This is exactly the kind of thing worth recognizing rather than memorizing — if you open a Next.js project and see a folder that matches a URL path you know the site has, that's not a coincidence.

---

## Hands-On Lab

**Deck:** [Slide 10](slides.html#s10)

Rebuild the church tool from Session 3's homework as React components — same idea, now with props and state doing the work instead of manual DOM calls:

1. `npm create vite@latest` a fresh app (or extend one already started)
2. Break the tool into at least **two components** — e.g. a list component that takes items as props, and an item component with its own local state (checked/signed-up/done)
3. Get it running with `npm run dev`, confirm hot reload actually updates the browser when you save
4. Ship it the same way as always: branch → Claude helps write it → you review the diff → commit → push → PR → CI (Session 2) → merge

Same constraint as Session 3: **it ships as a real PR.** The component structure is the point, not a polished feature.

---

## Quick Reference Card (keep this open while working)

**Deck:** none — reference material

```
# starting a fresh Vite + React project
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev

# props vs. state
props  -> passed in from a parent, read-only here
state  -> owned by this component, changes trigger a re-render

# recognizing a non-Vite project (check package.json "scripts")
"start": "craco start"   -> Create React App + Craco, use `npm start`
"dev": "vite"             -> Vite, use `npm run dev`
"dev": "next dev"         -> Next.js, use `npm run dev`

# routing
Vite      -> add react-router, wire up routes yourself
Next.js   -> file-based: app/schedule/page.jsx  =>  /schedule
```

---

## Homework Before Next Session

**Deck:** [Slide 11](slides.html#s11)

- [ ] Get the Session 3 tool running as React components, with at least one prop and one piece of state
- [ ] Open a project (yours, a teammate's, or idmc-gcfsm's `README`/`package.json`) and identify which tool it uses — Vite, Next.js, or CRA/Craco — from the `scripts` section alone
- [ ] Same PR discipline: branch, review, ship through CI
