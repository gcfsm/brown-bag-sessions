# Sandbox — Shared Practice Repo

The shared practice project is a **separate repo**, not this folder:

**[github.com/gcfsm/brown-bag-sandbox](https://github.com/gcfsm/brown-bag-sandbox)**

Each attendee forks it once, in Session 1, and builds on that same fork
across every session — it's their project, not a fresh clone each time.
This folder just documents that decision so it isn't lost.

## Required seed — Session 2 fails without it

**The sandbox repo must ship a `package.json` before anyone runs Session 2.**
This bit us live: Session 2 has attendees add a `ci.yml` that runs
`npm install`, `npm run lint`, `npm test`. A fork with no `package.json`
fails on the *first* step with `ENOENT`, and the red X reads
`lint-and-test` even though neither lint nor test ever ran.

Session 2's notes now walk through creating these files, so the session is
self-sufficient either way — but seeding them in the sandbox repo means
attendees hit the CI lesson instead of the missing-file lesson.

Three files, **no dependencies to install** (`node --check` and `node --test`
are built into Node):

- `package.json` — `"lint": "node --check src/greet.js"`, `"test": "node --test"`
- `src/greet.js` — a `greet(name)` function, exported
- `test/greet.test.js` — one assertion against it

Also commit `package-lock.json` (run `npm install` once to generate it) —
Session 2 Section 3 adds `cache: 'npm'`, which is keyed off the lock file.
Full contents are in [Session 2, Section 2](../sessions/02-cicd-actions/README.md#2-your-first-workflow-lintest).

Deliberately trivial: it exists so the check has something real to verify and
so Session 2's "break it on purpose and read the failed run" homework has
something to break. Real code arrives in Session 3.

Still TBD, to fill in as later sessions are written:
- [ ] Apply the seed above to `gcfsm/brown-bag-sandbox`
- [ ] Seed data for Firestore exercises (Session 5-6)
- [ ] Whether the scaffold needs a framework added before Session 4, or
      attendees add it themselves live in that session
