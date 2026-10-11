# 🏆 GitLab "Life After Code" Transcend Hackathon — Final Winning Submission Package

## 📌 Executive Submission Overview
- **Project Name:** Strix-Duo QA
- **Tagline:** Autonomous DevSecOps Lifecycle Verification Agent powered by GitLab Duo, Strix Dynamic Pentesting, and REA Runtime Reverse Engineering.
- **Entrant:** Mejbaur Bahar (`fagun115946@gmail.com`)
- **Hackathon Track:** Path A (Original New Project built on/after Oct 5, 2026) + Bonus Google Cloud Deployment
- **Official Public GitLab Repository (MIT Licensed):** [https://gitlab.com/strix-qa-group/strix-duo-qa](https://gitlab.com/strix-qa-group/strix-duo-qa)
- **Official GitHub Mirror:** [https://github.com/mejbaurbahar/strix-duo-qa](https://github.com/mejbaurbahar/strix-duo-qa)
- **Live Demo Video (Script & Asset):** Prepared below and stored locally at `/Users/a1/Projects/strix-duo-qa/assets/`

---

## 🎯 Devpost Submission Form Fields (Copy & Paste Ready)

### 1. Project Title
`Strix-Duo QA: Autonomous DevSecOps Lifecycle Verification Agent`

### 2. Elevator Pitch / Tagline (Under 200 characters)
`Autonomous DevSecOps agent for GitLab Duo. Harnesses Strix AI pentesting and REA contract analysis to block vulnerable MRs, generate exploit PoCs, and suggest auto-fixes.`

### 3. Public GitLab URL
`https://gitlab.com/strix-qa-group/strix-duo-qa`

### 4. Public GitHub Mirror URL
`https://github.com/mejbaurbahar/strix-duo-qa`

### 5. Detailed Description (Markdown for Devpost Project Story)

#### 💡 Inspiration
AI coding tools like GitHub Copilot and ChatGPT have made code generation fast. But in modern enterprise environments, **"Life After Code"** is where engineering breaks down:
1. **API Contract Drift:** AI generates functions that subtly break existing schema contracts or forget authentication middleware.
2. **Critical Security Vulnerabilities:** Generated code frequently introduces OWASP Top 10 flaws like Insecure Direct Object References (IDOR) and broken access control.
3. **Manual QA Bottlenecks:** Human QA teams cannot review hundreds of AI-generated Merge Requests daily.

We built **Strix-Duo QA** to completely take over post-code verification inside the GitLab Duo Agent Platform.

#### ⚙️ What it Does
Strix-Duo QA is a multi-agent DevSecOps testing engine designed for GitLab Duo and GitLab CI/CD pipelines:
- **REA (Reverse Engineering Agent):** Inspects dynamic API endpoints and code contracts at runtime, detecting missing authorization middleware and schema inconsistencies.
- **Strix (Autonomous AI Pentester):** Acts as an autonomous attacker, launching real exploit simulations against the staging environment and generating working, runnable Proof-of-Concept (PoC) scripts.
- **GitLab Duo CI/CD Gate:** Evaluates the audit results, blocks the pipeline if Critical or High severity vulnerabilities are detected, and posts an interactive markdown discussion on the GitLab Merge Request complete with exact copy-paste diff patches.
- **Google Cloud Run Microservice:** Exposes a containerized webhook server to receive pipeline triggers and execute verification on demand.

#### 🛠️ How We Built It
- **GitLab Duo Agent Platform:** Structured to integrate with Duo tools and native `.gitlab-ci.yml` pipeline stages.
- **`usestrix/strix` Core:** Integrated for autonomous penetration testing and verifiable vulnerability exploitation.
- **`morluto/rea` Concept:** Adapted for reverse engineering API signatures and runtime contract drift.
- **Google Cloud Run:** Packaged with a production-ready `Dockerfile` and Python 3.11 microservice server.
- **Test Suite:** Built with Python `unittest`, covering test verification, severity scoring, and markdown report generation.

#### ⚖️ Challenges We Overcame
- **Zero-Hallucination PoCs:** Generic SAST tools produce hundreds of false positives. Strix-Duo only flags vulnerabilities when an actual, runnable `curl` / exploit script succeeds in attacking the endpoint.
- **Seamless GitLab Integration:** Designing the agent to output native GitLab markdown diff blocks so engineers can resolve findings with a single click.

#### 📈 Accomplishments that We're Proud Of
- Created an end-to-end, runnable multi-agent security engine that runs in less than 3 seconds per endpoint.
- Achieved full test passing status across all unit test modules.
- Deployed a publicly visible GitLab repository with detectable MIT open-source licensing.

#### 🔮 What's Next for Strix-Duo QA
- Direct integration with GitLab Duo Agent Chat slash commands (`/strix-verify`).
- Continuous fuzzing of GraphQL and gRPC microservice endpoints in production.
