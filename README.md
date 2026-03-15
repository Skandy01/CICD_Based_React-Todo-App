# 🚀 Production-Grade DevSecOps CI/CD Pipeline  
**Full-Stack Application Delivery with Azure DevOps & GitHub Actions**

> **Real enterprise delivery is hard. This repo proves you can do it right.**

---

## Why This Repository Exists

In most companies, building the app is the easy part.  
**Delivering it securely, reliably, and at scale** — that’s the real challenge.

This repository is **intentionally** designed with a **simple application** but an **extremely robust, production-grade pipeline**.

- The **app** is kept minimal on purpose.  
- The **pipeline** is deliberately complex and enterprise-ready.

Focus = **DevSecOps, quality gates, artifact governance, approval workflows, and VM-based deployments** — not fancy UI features.

---

## 🧠 Real-World Problem This Solves

Modern delivery teams constantly struggle with:

- **Vulnerable dependencies** slipping into production  
- **Inconsistent quality** across frontend, backend, Docker, and YAML  
- **Lack of auditability** and manual approval controls  
- **Reliable deployments** to long-lived environments (VMs, EC2, etc.)  
- **Balancing velocity with security & compliance**

This repo shows exactly how to solve all of the above using industry best practices.

---

## 🏗️ Application Overview (Just the Delivery Vehicle)

| Layer          | Technology                  | Purpose                     |
|----------------|-----------------------------|-----------------------------|
| **Frontend**   | React + Vite                | Modern SPA                  |
| **Backend**    | Python FastAPI              | REST API                    |
| **Container**  | Docker                      | Consistent packaging        |
| **Deployment** | Azure Virtual Machines      | Real-world VM target        |
| **Extensible** | AWS EC2, Kubernetes, AKS    | Easy to adapt               |

---

## 🔄 What This Repository Demonstrates (The Real Value)

This is **not** a toy/demo pipeline. This is a **production-grade delivery pipeline** that mirrors what top companies actually run.

### ✅ Enterprise Capabilities Shown

- Multi-stage pipeline architecture  
- Software Composition Analysis (SCA)  
- Static Application Security Testing (SAST)  
- Comprehensive linting & quality enforcement  
- Immutable artifact strategy  
- Manual approval gates + environment protection  
- VM-based deployment automation  
- Secret-free repository (everything via Variable Groups & Service Connections)

---

## 🧩 CI/CD Architecture

**Primary Pipeline:** `.azure-pipelines/production-grade-pipeline.yml`

The pipeline is split into **clear, auditable stages**:

### Pipeline Stages

1. **Software Composition Analysis**  
   - Dependency vulnerability scanning using **Retire.js** (frontend + backend)

2. **Static Code Analysis**  
   - **SonarQube / SonarCloud** for code quality, bugs, security hotspots, and technical debt

3. **Code Quality & Linting** (Non-blocking where appropriate)
   - Frontend: ESLint + Stylelint + Biome
   - Backend: PyLint + Black + isort
   - Docker: Hadolint
   - Docs: MarkdownLint + YAMLlint

4. **Build & Artifact Packaging**
   - Frontend → versioned build artifact
   - Backend → versioned Python package + Docker image (optional)

5. **Approval Gate**
   - Manual validation using **Azure DevOps Environments** (change control + audit)

6. **Deploy to Dev / Staging / Prod**
   - Secure copy to VM web directory
   - Backend service restart with systemd
   - Health-check validation

---

## 📦 Deployment Strategy

- **CI** produces immutable, versioned artifacts  
- **CD** consumes those artifacts only (no rebuilding in release stage)  
- Uses **Azure DevOps Environments** for deployment gates and history  
- Works exactly the same on **Azure VMs**, **AWS EC2**, or even bare-metal

Perfect for companies still running hybrid/legacy VM fleets.

---

## 🔐 Security & Governance (Zero Compromise)

- **No secrets** ever committed to Git  
- All credentials via:
  - Azure DevOps **Variable Groups**
  - **Service Connections** (Azure RM, GitHub, etc.)
- Planned upgrade: **OIDC + Workload Identity Federation** (passwordless Azure access)

Every deployment is fully auditable.

---

## 🧭 Design Decisions & Trade-offs (Why we did it this way)

| Decision                     | Reason                                      | Trade-off                          |
|-----------------------------|---------------------------------------------|------------------------------------|
| VM-based deployment         | Mirrors real enterprise environments        | Not Kubernetes-native (by design)  |
| Non-blocking linting        | Developer-friendly while still visible      | Issues visible but don't fail CI   |
| Manual approval gates       | Required in regulated/enterprise setups     | Slight delay (intentional)         |
| Simple app code             | Focus 100% on pipeline & DevSecOps          | Not a feature-rich demo app        |

---

## 🔮 Future Enhancements (Roadmap)

- [ ] Kubernetes deployment stage (AKS/EKS)
- [ ] OIDC federated authentication
- [ ] GitHub Actions version of the same pipeline (multi-platform)
- [ ] Terraform infrastructure-as-code for VM provisioning
- [ ] Multi-region blue-green deployment
- [ ] DAST + runtime security scanning

---

## 👤 Author

**Skand Tripathi**  
*DevOps Engineer | CI/CD | Terraform | Azure | DevSecOps Specialist*

---

## ⭐ How to Use This Repo

1. Fork / clone the repository  
2. Update Azure DevOps service connections & variable groups  
3. Import the `production-grade-pipeline.yml`  
4. Watch the full DevSecOps magic happen automatically

---

**This is how real companies ship securely.**  
Not just "it works on my machine" — but **"it works in production with governance"**.

---

**Made with ❤️ for teams who want to level up their delivery game.**

---

*Feel free to star ⭐ the repo if this helped you understand enterprise-grade pipelines!*
