# Master Curriculum — GCF IT Community

Biweekly cadence. ~20 sessions across four blocks, followed by real project pairing.

Status legend: `[ ]` not started · `[~]` in progress · `[x]` ready to teach

---

## Block A — Foundations

| # | Session | Status | Folder |
|---|---|---|---|
| 1 | Git Basics — Fork, Clone, npm Packages, Branch, Push, PR, Code Review, Conflict Resolution | [x] | [`01-git-basics`](./sessions/01-git-basics) |
| 2 | CI/CD & GitHub Actions (free-tier features, lint/test workflows, CI Lint, Dependabot) | [x] | [`02-cicd-actions`](./sessions/02-cicd-actions) |
| 3 | Vibe Coding Your First App (with Claude) | [x] | [`03-vibe-coding-first-app`](./sessions/03-vibe-coding-first-app) |
| 4 | React on Firebase — JS History, Vite vs. Next.js, and Where Each One Deploys | [x] | [`04-react-vite-nextjs-basics`](./sessions/04-react-vite-nextjs-basics) |
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
| 11 | Claude Skills, Hooks, Githooks, Agentic Loops, MCP Servers, Routines | [ ] | [`11-claude-skills-hooks-agentic`](./sessions/11-claude-skills-hooks-agentic) |

## Block E — Professional Practice

| # | Session | Status | Folder |
|---|---|---|---|
| 12 | Testing & QA (Jest/Vitest, tying into CI/CD) | [ ] | [`12-testing-qa`](./sessions/12-testing-qa) |
| 13 | Data Privacy & RA 10173 (Philippine Data Privacy Act) | [ ] | [`13-data-privacy-ra10173`](./sessions/13-data-privacy-ra10173) |
| 14 | Documentation & Technical Writing | [ ] | [`14-documentation-technical-writing`](./sessions/14-documentation-technical-writing) |
| 15 | Monitoring & Observability Basics (uptime, heartbeats, on-call, status pages) + Disaster Recovery (Firestore backups) | [ ] | [`15-monitoring-observability`](./sessions/15-monitoring-observability) |
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
- Uptime monitoring added to Session 15 as the outside-in half of detection: logs and error tracking only report if the app is healthy enough to report, so an external check is the only thing that notices a total outage. Heartbeats are included specifically because they are what catches the Session 15 Firestore export silently no longer running — the two halves of this session check each other. On-call and escalation are covered at honest small-team scale rather than enterprise rotation. Better Stack is the concrete instance (it is what Ocean runs), taught concept-first so the tool stays swappable.
- Disaster Recovery / Firestore backups placed in Session 15 rather than Session 7 — paired with Observability since detection and recovery are two halves of the same production-readiness concern, not a Firestore feature tour.
- reCAPTCHA placed in Session 10 (App Check) since it's specifically an App Check verification provider; its free tier quota angle is cross-referenced in Session 16 (Cost Awareness) rather than duplicated.
- Routines added to the end of Session 11, after the MCP server build rather than beside it. The session already moves Skill (knowledge) to MCP server (tools); a routine is the third step (it starts itself), and that only reads as a step once they have built the thing that gets started. The teaching weight is on scoping, not scheduling: routines run with no permission prompts, attach every connector by default, and act under the user's own GitHub and connector identity. Also draws the line against CI from Session 2 explicitly — CI is a deterministic gate that blocks a merge, a routine is judgment that proposes, and a routine should never be the check that has to pass. This pushes Session 11 past a single hour, so the Part A / Part B split is now assumed rather than flagged.
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
- Session 2 now creates a minimal `package.json` (plus one source file and one test) *before* the workflow file, because running it live surfaced a real break: a fresh sandbox fork has nothing for `npm install` to read, so the very first step fails with `ENOENT` and the check reports as `lint-and-test` failing even though neither ever ran. Deliberately zero-dependency — `node --check` for lint, `node --test` for test, both built into Node — so Session 2 stays about the CI mechanism rather than about configuring ESLint, and so the "break it on purpose and read the failed run" homework has something real to break. The failure is kept as a teaching beat rather than just fixed: a check is only as real as the thing it runs, and CI reporting "nothing to verify" is CI working correctly. The sandbox repo should carry the same seed (see `sandbox/README.md`).
- Branch protection is deliberately split across Session 1 and Session 2 rather than taught once: Session 1 states the concept (why a PR isn't optional) where the PR/review workflow is already being taught; Session 2 does the hands-on setup, since "require status checks" needs a real CI check (built earlier in Session 2) to attach to.
- Session 3 opens by explicitly cashing in Session 1 and 2's "AI-assisted coding makes Git more important, not less" claim rather than re-arguing it — the two safety nets exist *before* Session 3 starts on purpose, so letting Claude drive fast is a tested claim, not a gamble.
- Session 3's hands-on examples are church-relevant (RSVP tally, volunteer sign-up list) at the same tiny technical scope as a generic calculator would be — free to do, and starts "I build things for the church" on day one of AI-assisted work instead of waiting for Session 4+'s real stack.
- Session 4 carries **no code at all** — a deliberate consequence of Session 3. Once Session 3 establishes that you state the what and the constraints and Claude writes the implementation, handing attendees JSX to memorise two weeks later contradicts the workflow the whole track is built on. What can't be delegated is the decision made *before* the prompt, so that is what Session 4 teaches: React vocabulary at the level needed to direct and review (component, props, state, route, and "where does state live"), and then the framework choice itself.
- Session 4 reframes Vite vs. Next.js as a **Firebase deployment decision**, not a taste one — which is also where the stack gets restated, since the Firebase commitment is easy to forget was ever a choice. Vite produces static files → **Firebase Hosting** (Spark/free tier viable, CDN only, no server, so server-side work means a *separate* Cloud Function); Next.js produces a running app → **Firebase App Hosting** (Blaze required, Cloud Run + Cloud Build underneath, git-triggered deploys, API routes included). Two honest guards against a too-clean rule: Next.js's API routes replace the endpoint you *call*, never the event-triggered or scheduled function (which forward-links to Session 7's trigger taxonomy), and Blaze means metered rather than expensive (forward-links to Session 16). Deployment *mechanics* stay in Session 7 — Session 4 only names the products and the consequences of the choice.
- Session 4 opens with a four-era history of JavaScript on the web — server-rendered pages with JS as garnish (Prototype/jQuery), the SPA (Backbone/AngularJS), Node.js putting JS on the server, then the component era (React/Vue) — landing on server rendering returning as era one's answer rebuilt with era four's tools. This exists to make the Vite/Next.js fork feel inevitable rather than arbitrary: the two options are two different eras' answers, which is *why* they need different Firebase products. It also earns the Session 3 hook, since the manual DOM code attendees wrote there is literally the era-one style. The README carries a facilitator note on where the four-era frame is simplified (era one never ended; Node predates AngularJS; Next.js packaged server rendering rather than inventing it; the Vite=SPA / Next=SSR mapping is a teaching device), so pushback from anyone who lived through it can be conceded accurately rather than argued with.
- Session 4 states the SEO argument in its current form rather than its 2010 form: Googlebot does render JavaScript, on a queued second pass, so a client-side app is **delayed and less certain to be indexed, not invisible** — with interaction-gated content still unseen and non-Google crawlers (Bing, social link previews, AI crawlers) further behind. The recommendation is unchanged, but the reasoning survives contact with someone who knows the modern behaviour.
- Session 4 keeps functional recognition for projects attendees didn't set up (Vite vs. Next.js vs. CRA/Craco — CRA being what the real target project, idmc-gcfsm, actually uses), but reaches it by asking Claude "what is this project, where does it deploy, does it have server-side code" rather than by reading build config. This does not extend to Sessions 1-2, which stay hand-typed/no-AI-shortcuts by design.
