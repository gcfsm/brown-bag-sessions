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
