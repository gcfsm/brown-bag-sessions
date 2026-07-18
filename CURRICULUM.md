# Master Curriculum — IT Group Hub

Biweekly cadence. ~20 sessions across four blocks, followed by real project pairing.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` ready to teach

---

## Block A — Foundations

| # | Session | Status | Folder |
|---|---|---|---|
| 1 | Git Basics — Fork, Clone, npm Packages, Branch, Push, PR, Code Review, Conflict Resolution | [x] | [`01-git-basics`](./sessions/01-git-basics) |
| 2 | CI/CD & GitHub Actions (free-tier features, lint/test workflows, CI Lint, Dependabot) | [x] | [`02-cicd-actions`](./sessions/02-cicd-actions) |
| 3 | Vibe Coding Your First App (with Claude) | [x] | [`03-vibe-coding-first-app`](./sessions/03-vibe-coding-first-app) |
| 4 | React / Vite / Next.js Basics | [x] | [`04-react-vite-nextjs-basics`](./sessions/04-react-vite-nextjs-basics) |
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
| 11 | Claude Skills, Hooks, Githooks, Agentic Loops, MCP Servers | [ ] | [`11-claude-skills-hooks-agentic`](./sessions/11-claude-skills-hooks-agentic) |

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
- MCP Servers added to Session 11 rather than a new session — it's the natural next step after Skills/Hooks/Agentic Loops (giving Claude callable tools, not just instructions). Also flagged as a split candidate given the session's growing density.
- Session 1 opens with a "why Git exists" hook — the pre-Git file-naming pain (`proposal_FINAL_v2_ACTUALLY_FINAL.docx`) — before any commands are introduced, so every technical concept that follows has a concrete problem it's solving.
- npm packages added to Session 1 (right after Fork/Clone) rather than Session 4 — it's the practical next step after cloning any repo, and `node_modules` being gitignored is a natural extension of the Git "source of truth vs. regeneratable output" concept already being taught.
- CVS and SVN added to Session 1's "Why Git Exists" intro as the missing historical middle step between manual file-naming chaos and Git — frames Git's distributed model (cheap branching/merging) as a direct response to the centralized model's limitations, which sets up why the fork/branch/PR workflow works the way it does.
- Session 1's intro closes with an explicit link from Git history to vibe coding/AI-assisted dev — Git's history/branches/diffs/commits are framed as the safety net that makes AI-assisted changes reviewable and reversible, directly setting up Session 3 (Vibe Coding) and Session 11 (Agentic workflows) rather than presenting Git as a standalone skill.
- Session 1 uses this very curriculum-building conversation as a concrete example of Git's value for AI-assisted iteration (commit-by-commit building, versus re-sending whole files).
- `git worktree` introduced conceptually (name + why it matters) in Session 1, with the hands-on application deferred to Session 11 where it's actually useful — running parallel Claude sessions on separate branches without constant stashing/switching.
- Session 10 (Security/Cloudflare/RBAC-adjacent) is placed after Block A/B so attendees have something real to secure.
- Session 16 (Cost Awareness) builds on the indexes intro from Session 6 rather than re-teaching what an index is.
- Session 19 (Epics & ACs) is the unlock, not just "another topic" — attendees can informally start pairing on real tickets as soon as they're ready, even before Session 20 formally happens.
- Session 2 opens with "integration hell" — the pre-CI pain of infrequent, all-at-once merges — as the direct sequel to Session 1's "cheap branching/merging" close: Git makes merging cheap, but only CI makes merging *often* safe, which is why the two sessions are back-to-back rather than CI/CD being deferred to the Professional Practice block.
- Branch protection is deliberately split across Session 1 and Session 2 rather than taught once: Session 1 states the concept (why a PR isn't optional) where the PR/review workflow is already being taught; Session 2 does the hands-on setup, since "require status checks" needs a real CI check (built earlier in Session 2) to attach to.
- Session 3 opens by explicitly cashing in Session 1 and 2's "AI-assisted coding makes Git more important, not less" claim rather than re-arguing it — the two safety nets exist *before* Session 3 starts on purpose, so letting Claude drive fast is a tested claim, not a leap of faith.
- Session 3's hands-on examples are church-relevant (RSVP tally, volunteer sign-up list) at the same tiny technical scope as a generic calculator would be — free to do, and starts "I build things for the church" on day one of AI-assisted work instead of waiting for Session 4+'s real stack.
- Session 4 is deliberately kept light on build-tool internals (Vite vs. Create React App/Craco, which is what the real target project — idmc-gcfsm — actually uses) rather than a deep platform-comparison section: since attendees vibe-code most implementation work, they need functional recognition (what command runs this, what file configures it) rather than mastery of either tool's internals. This does not extend to Sessions 1-2, which stay hand-typed/no-AI-shortcuts by design.
