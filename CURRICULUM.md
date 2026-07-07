# Master Curriculum — IT Group Hub

Biweekly cadence. ~20 sessions across four blocks, followed by real project pairing.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` ready to teach

---

## Block A — Foundations

| # | Session | Status | Folder |
|---|---|---|---|
| 1 | Git Basics — Fork, Clone, Branch, Push, PR, Code Review, Conflict Resolution | [x] | [`01-git-basics`](./sessions/01-git-basics) |
| 2 | CI/CD & GitHub Actions (free-tier features, lint/test workflows, CI Lint, Dependabot) | [ ] | [`02-cicd-actions`](./sessions/02-cicd-actions) |
| 3 | Vibe Coding Your First App (with Claude) | [ ] | [`03-vibe-coding-first-app`](./sessions/03-vibe-coding-first-app) |
| 4 | React / Vite / Next.js Basics | [ ] | [`04-react-vite-nextjs-basics`](./sessions/04-react-vite-nextjs-basics) |
| 5 | Data Modeling & NoSQL Patterns | [ ] | [`05-data-modeling-nosql`](./sessions/05-data-modeling-nosql) |

## Block B — Firebase & Infra

| # | Session | Status | Folder |
|---|---|---|---|
| 6 | Firebase / Firestore / Auth Basics (incl. Indexes intro) | [ ] | [`06-firebase-firestore-auth-basics`](./sessions/06-firebase-firestore-auth-basics) |
| 7 | Firebase Deeper — Storage, Secret Manager, Custom Domain, Cloud Functions, Deploy CI/CD | [ ] | [`07-firebase-storage-secrets-deploy`](./sessions/07-firebase-storage-secrets-deploy) |
| 8 | Multi-Tenant Architecture | [ ] | [`08-multi-tenant-architecture`](./sessions/08-multi-tenant-architecture) |

## Block C — Security

| # | Session | Status | Folder |
|---|---|---|---|
| 9 | RBAC & Auth Patterns | [ ] | [`09-rbac-auth-patterns`](./sessions/09-rbac-auth-patterns) |
| 10 | Cloudflare, App Check, IP Limiting (incl. reCAPTCHA + free tier quota) | [ ] | [`10-cloudflare-appcheck-ip-limiting`](./sessions/10-cloudflare-appcheck-ip-limiting) |

## Block D — AI-Native Workflow

| # | Session | Status | Folder |
|---|---|---|---|
| 11 | Claude Skills, Hooks, Githooks, Agentic Loops | [ ] | [`11-claude-skills-hooks-agentic`](./sessions/11-claude-skills-hooks-agentic) |

## Block E — Professional Practice

| # | Session | Status | Folder |
|---|---|---|---|
| 12 | Testing & QA (Jest/Vitest, tying into CI/CD) | [ ] | [`12-testing-qa`](./sessions/12-testing-qa) |
| 13 | Data Privacy & RA 10173 (Philippine Data Privacy Act) | [ ] | [`13-data-privacy-ra10173`](./sessions/13-data-privacy-ra10173) |
| 14 | Documentation & Technical Writing | [ ] | [`14-documentation-technical-writing`](./sessions/14-documentation-technical-writing) |
| 15 | Monitoring & Observability Basics + Disaster Recovery (Firestore backups) | [ ] | [`15-monitoring-observability`](./sessions/15-monitoring-observability) |
| 16 | Cost Awareness (indexes cost/perf, reads/writes, cold starts) | [ ] | [`16-cost-awareness`](./sessions/16-cost-awareness) |

## Block F — Career & Design

| # | Session | Status | Folder |
|---|---|---|---|
| 17 | Design / UX Fundamentals | [ ] | [`17-design-ux-fundamentals`](./sessions/17-design-ux-fundamentals) |
| 18 | Career Track — Portfolio, Resume, Interviews, Open Source Etiquette | [ ] | [`18-career-track`](./sessions/18-career-track) |

## Block G — The Gate

| # | Session | Status | Folder |
|---|---|---|---|
| 19 | Planning — Epics & Acceptance Criteria (Ocean's Method) | [ ] | [`19-planning-epics-acs`](./sessions/19-planning-epics-acs) |
| 20 | Capstone — Pairing on a Real Church Project Ticket | [ ] | [`20-capstone-real-project`](./sessions/20-capstone-real-project) |

---

## Notes on Sequencing

- Session 3 (Vibe Coding) is placed early intentionally — it's the momentum/hook session, not a reward for finishing fundamentals.
- Session 5 (Data Modeling) is placed before Firebase proper — most Firestore mistakes are modeling mistakes, not API mistakes.
- Session 8 (Multi-Tenant) gets its own session rather than being folded into Firebase basics — it is genuinely advanced.
- Session 7 now includes a serverless-vs-servers comparison plus Cloud Functions on top of Storage/Secrets/Domain/Deploy — flagged in its README as a candidate to split into two parts if running strict 1hr sessions.
- Disaster Recovery / Firestore backups placed in Session 15 rather than Session 7 — paired with Observability since detection and recovery are two halves of the same production-readiness concern, not a Firestore feature tour.
- reCAPTCHA placed in Session 10 (App Check) since it's specifically an App Check verification provider; its free tier quota angle is cross-referenced in Session 16 (Cost Awareness) rather than duplicated.
- Session 10 (Security/Cloudflare/RBAC-adjacent) is placed after Block A/B so attendees have something real to secure.
- Session 16 (Cost Awareness) builds on the indexes intro from Session 6 rather than re-teaching what an index is.
- Session 19 (Epics & ACs) is the unlock, not just "another topic" — attendees can informally start pairing on real tickets as soon as they're ready, even before Session 20 formally happens.
