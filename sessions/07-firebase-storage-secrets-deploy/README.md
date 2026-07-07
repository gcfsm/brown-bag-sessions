# Session: Firebase Deeper — Storage, Secret Manager, Custom Domain, Cloud Functions, Deploy CI/CD

**Status:** [ ] Not started

## Goal

Go beyond Firestore basics into Storage, secret management, custom domains,
Cloud Functions, and deployment pipelines — including understanding when
serverless is the right call versus a traditional cloud server.

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
    - **HTTP-triggered** — plain HTTP endpoint, called via fetch/axios from anywhere, you handle auth/CORS yourself
    - **onCall (Callable functions)** — Firebase SDK handles auth token passing and serialization for you; called via `httpsCallable()` from the client, not a raw URL; preferred for client-app-to-backend calls
    - **Event-triggered (Firestore/Storage/Auth)** — fires automatically on a data event (onCreate/onUpdate/onDelete for Firestore, file upload for Storage, new user for Auth); no direct client call, runs in response to a change
    - **Scheduled functions** — runs on a cron-like schedule via Cloud Scheduler / Pub/Sub, not triggered by a client or a data event at all (e.g. nightly cleanup, daily digest email)
  - When to use which — client-initiated action → onCall; reacting to data changes → event-triggered; time-based/recurring job → scheduled; public webhook or third-party integration → HTTP
  - Local emulation and testing before deploy
  - Cold start behavior in practice
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
Serverless comparison + Cloud Functions + Deploy CI/CD). Consider splitting
into two 1hr parts if running strictly to the 1hr format:
- **Part A:** Storage, Secret Manager, Custom Domain
- **Part B:** Serverless vs. servers comparison, Cloud Functions, Deploy CI/CD

