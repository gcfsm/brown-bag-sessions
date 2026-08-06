# Session: Monitoring & Observability Basics + Disaster Recovery

**Status:** [ ] Not started

## Goal

Understand how to know when something breaks in production, basic tools for
finding out, and how to recover data when things go wrong — detection and
recovery as two halves of the same production-readiness concern.

## Prerequisites

Sessions 6-7 (something deployed to monitor)

## Topics to Cover (outline — expand with full detail)

- Why observability matters
- Basic logging practices
- Error tracking concepts
- "How do you find out something's wrong before a user tells you"
- Light tool overview (no deep dive)
- **Uptime Monitoring — checking from the outside**
  - The distinction that organises this session: logs and error tracking are
    *inside* the app and only report if the app is running well enough to
    report. An uptime monitor is *outside* it, hitting a URL on a schedule.
    If the whole thing is down, only the outside check notices
  - **Monitors** — one per public URL, on an interval. The interval sets your
    worst-case blind window: a 30-minute check means up to 30 minutes of
    downtime before anyone is told. Shorter costs more and gets noisier —
    naming that trade-off out loud is the lesson, not picking a number
  - **Heartbeats** — the check inverted. Instead of something reaching in to
    your service, your job reaches *out* on a schedule, and the alert fires
    when the ping stops. This is the only thing that catches a scheduled task
    that silently stopped running — including the Firestore export below,
    which fails silently by default
  - **Incidents, on-call, escalation policies** — who finds out, how, and who
    gets told next when the first person doesn't answer. Worth covering even
    at church-volunteer scale, where the honest answer may be "one person,
    and here's what happens when they're on holiday"
  - **Status pages** — the public artifact. Turns "is it just me?" into a link,
    and gives you an uptime record over time
  - Ocean runs Better Stack for all of the above — use it as the concrete
    instance, but teach the concepts so the tool is swappable
- **Disaster Recovery & Firestore Backups**
  - What DR means in practice for a small team (not enterprise-scale DR — realistic scope)
  - Firestore scheduled exports to Cloud Storage — setting one up
  - Manual export/import basics
  - RPO/RTO in plain terms — "how much data could we lose" and "how long to recover"
  - Restore process walkthrough (at least conceptually, ideally hands-on in sandbox)
  - Why backups matter even on a platform that feels "managed" (accidental deletes, bad deploys, human error — not just server failure)

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
