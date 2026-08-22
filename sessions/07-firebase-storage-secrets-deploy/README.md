# Session: Firebase Deeper — Storage, Secret Manager, Custom Domain, Environments (Dev/Prod), Cloud Functions, Deploy CI/CD

**Status:** [ ] Not started

## Goal

Go beyond Firestore basics into Storage, secret management, custom domains,
running separate dev and prod environments, Cloud Functions, and deployment
pipelines — including understanding when serverless is the right call versus a
traditional cloud server.

## Prerequisites

Session 6

## Topics to Cover (outline — expand with full detail)

- Firebase Storage basics
- Secret Manager — storing and referencing secrets safely
- Custom domain setup
- **Serverless vs. traditional cloud servers — comparison**
  - Serverless (Cloud Functions) vs. VMs/containers (Compute Engine, Cloud Run, traditional VPS)
  - Cold starts vs. always-on — tradeoffs
  - Pricing model differences (pay-per-invocation vs. pay-for-uptime)
  - When serverless makes sense (event-driven, bursty, low-maintenance) vs. when it doesn't (long-running processes, heavy compute, predictable high load)
  - Where Cloud Run sits as a middle ground (containerized, still scales to zero)
- **Firebase Cloud Functions**
  - **Trigger types — clear distinctions:**
    - **Triggers (event-triggered)** — the function fires *automatically* when something happens to data on the backend: a document created/updated/deleted in Firestore, a file uploaded to Storage, a user created in Auth. Nobody calls it directly — it reacts to a change. This is what "trigger" means when used precisely; teach this definition first since the term gets used loosely elsewhere.
    - **HTTP-triggered** — plain HTTP endpoint, called via fetch/axios from anywhere, you handle auth/CORS yourself. Confusingly also has "triggered" in the name, but it's *called*, not reactive — worth flagging this naming overlap explicitly so attendees don't conflate it with true event triggers.
    - **onCall (Callable functions)** — Firebase SDK handles auth token passing and serialization for you; called via `httpsCallable()` from the client, not a raw URL; preferred for client-app-to-backend calls
    - **Scheduled functions** — runs on a cron-like schedule via Cloud Scheduler / Pub/Sub, not triggered by a client or a data event at all (e.g. nightly cleanup, daily digest email)
  - When to use which — client-initiated action → onCall; reacting to data changes → event-triggered; time-based/recurring job → scheduled; public webhook or third-party integration → HTTP
  - Local emulation and testing before deploy
  - Cold start behavior in practice
- **Dev vs. Prod environments — running two separate Firebase projects**
  - **Why separate at all** — the point people miss until it bites them:
    - You never test rules, functions, or a schema change against **real
      people's data**. Dev is where a mistake is free; prod is where a mistake
      has someone's name and phone number in it (forward-links to Session 13,
      Data Privacy)
    - A broken deploy in dev doesn't take the **live church site** down. The
      blast radius of "oops" is the whole reason the split exists
  - **The mechanics — one Firebase project per environment**
    - Two projects, e.g. `gcf-app-dev` and `gcf-app-prod` — separate
      Firestore data, separate Auth users, separate everything. They are *not*
      two folders in one project; they are two projects
    - `.firebaserc` holds project **aliases**, so `firebase use dev` /
      `firebase use prod` switches which one you're pointed at, and
      `firebase deploy --project prod` is explicit at deploy time
    - The honest failure mode to warn about out loud: running a destructive
      command while pointed at prod because you forgot to check `firebase use`.
      Make "which project am I on?" a reflex
  - **Config differs per environment, and that's the whole game**
    - Separate secrets in Secret Manager (dev API keys ≠ prod API keys)
    - Separate `apphosting.yaml` / functions config values per project
    - Separate App Check registrations and reCAPTCHA keys (ties to Session 10)
  - **The promotion path — how a change gets from dev to prod**
    - CI (Session 2) deploys the dev branch to the **dev** project
      automatically, so every merge is exercised somewhere real but harmless
    - Prod deploy is gated: it happens only on a merge to the **production
      branch**, behind the same required checks and branch protection from
      Session 2 (this is where Session 4's "merging a PR ships to production"
      gets its guard rails)
  - **The honest small-church scope** — say this so nobody over-builds:
    **dev + prod is the sane minimum**, and it's worth the setup. A third
    "staging" environment is usually overkill at church-project scale — name
    it as a thing that exists at bigger companies, and skip it here until
    there's a real reason
- Deploy CI/CD — wiring Firebase deploy into GitHub Actions from Session 2

## Agenda (TBD)

- [ ] Intro / recap of previous session (5-10 min)
- [ ] Theory / demo segment (TBD)
- [ ] Hands-on lab segment (TBD)
- [ ] Wrap-up / homework assignment (5 min)

## Hands-On Lab (TBD)

_Describe the specific exercise attendees will do against the shared sandbox repo._

## Handout / Cheat Sheet (TBD)

_Link or embed a quick-reference handout, similar to Session 1's Quick Reference Card._

## Homework (TBD)

_What attendees should do before the next session._

## Facilitator Note

This session is now fairly dense (Storage + Secret Manager + Custom Domain +
Dev/Prod environments + Serverless comparison + Cloud Functions + Deploy
CI/CD). Consider splitting into two 1hr parts if running strictly to the 1hr
format:
- **Part A:** Storage, Secret Manager, Custom Domain
- **Part B:** Serverless vs. servers comparison, Cloud Functions, Dev/Prod
  environments, Deploy CI/CD

Dev/Prod environments sits in Part B next to Deploy CI/CD deliberately: the
two-project split only makes sense once you're actually deploying, since the
promotion path (dev branch → dev project, prod branch → prod project) *is* a
CI/CD wiring decision, not a separate topic.

