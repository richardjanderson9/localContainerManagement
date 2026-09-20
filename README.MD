# Local Container Management Public (`localContainerManagementPublic`)

A lightweight template repository designed to build, containerize, and automatically push a Python application to the Vultr Container Registry (VCR) using GitHub Actions.

---

## 🚀 Project Structure

```text
├── .github/
│   └── workflows/
│       └── deploy.yml   # Automated GitHub Actions build & push pipeline
├── app.py               # Simple Python hello-world script
├── Dockerfile           # Optimized, secure, non-root Docker configuration
├── .gitignore           # Excludes temporary cache and environment files
└── README.md            # Project documentation
```

---

## 🛠️ Tech Stack

* **Language:** Python 3.11 (Slim)
* **Containerization:** Docker (configured with a secure non-root user)
* **CI/CD:** GitHub Actions
* **Registry:** Vultr Container Registry (VCR)

---

## ⚙️ Automated CI/CD Pipeline

The GitHub Actions workflow triggers automatically when a push is made to the `main` branch that includes changes to:
* `.json` files
* `Dockerfile`
* Python (`.py`) files

### Pipeline Stages
1. **📥 Checkout Repository:** Pulls the latest project code.
2. **🔐 Log in to Vultr CR:** Authenticates with your private Vultr registry using GitHub Secrets.
3. **🏷️ Extract Metadata:** Generates `latest` and short-commit SHA tags for Docker.
4. **🚀 Build & Push:** Compiles the container image and pushes it securely to `usa.vultrcr.com/nameOfRepo/containerName`.

---

## 🔑 Required GitHub Secrets

To allow the workflow to push containers to your private Vultr Container Registry, configure the following **Repository Secrets** in your GitHub repository (**Settings > Secrets and variables > Actions**):

| Secret Name | Description |
| :--- | :--- |
| `VULTR_CR_SERVER` | Your Vultr registry domain endpoint (e.g., `usa.vultrcr.com`) |
| `VULTR_CR_USERNAME` | Your Vultr Container Registry username/UUID |
| `VULTR_CR_PASSWORD` | Your Vultr Container Registry API key / password 