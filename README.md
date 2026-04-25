# ⚛️ CERN Papers Search Engine

A production-ready, full-stack search engine for high energy physics research papers, powered by CERN's official Inspire-HEP API. Built to demonstrate real-world skills in Python backend development, search engine integration, containerization, and cloud-native deployment.

---

## 🌐 Live Demo
Coming soon — deploying on Koyeb

---

## 📌 What It Does

Type any physics topic — Higgs Boson, Dark Matter, LHC, Gravitational Waves — and instantly get the most recent or most cited research papers from CERN's official database.

Each result shows:
- Full paper title
- Authors
- Publication year
- Abstract preview
- Direct link to the full paper on arXiv

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python 3.12, FastAPI | REST API and server-side logic |
| Search Engine | OpenSearch 2.17 | Fast full-text search and indexing |
| Frontend | Jinja2, HTML5, CSS3 | Server-side rendered UI |
| HTTP Client | HTTPX | Async requests to Inspire-HEP API |
| Containerization | Docker | Isolated, reproducible environment |
| Orchestration | Docker Compose | Multi-container local deployment |
| Kubernetes | K8s Manifests | Production-grade orchestration |
| CI/CD | GitHub Actions | Automated build and deployment |
| Data Source | Inspire-HEP REST API | CERN's official HEP paper database |

---

## 🚀 Run Locally

Prerequisites:
- Docker Desktop
- Docker Compose

Steps:

git clone https://github.com/sushmithainjeti/cern-papers-search.git
cd cern-papers-search
docker-compose up --build

Open http://localhost:8000

---

## 📁 Project Structure

cern-papers-search/
├── main.py                 # FastAPI app
├── templates/
│   └── index.html          # Jinja2 HTML template
├── static/                 # Static assets
├── Dockerfile              # Container definition
├── docker-compose.yml      # Multi-container setup
├── k8s/                    # Kubernetes manifests
├── requirements.txt        # Python dependencies
└── .github/workflows/      # GitHub Actions CI/CD

---

## 🔍 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Home page |
| GET | /search?q={query}&sort={sort} | Search papers |

Sort options:
- mostrecent — Latest papers first
- mostcited — Most cited papers first

---

## 💡 Why This Project?

CERN's existing Inspire-HEP search interface is powerful but complex. This project builds a clean, accessible frontend on top of their public API making high energy physics research discoverable for students and researchers worldwide.

This aligns directly with CERN's open science mission and demonstrates practical skills relevant to CERN's IT and engineering teams:
- Working with real CERN APIs and data
- Production-grade containerization with Docker and Kubernetes
- OpenSearch which is used internally at CERN
- CI/CD automation with GitHub Actions

---

## 👩‍💻 Author

Sushmitha Injeti
📧 sushmithainjeti529@gmail.com

---

## 📄 License

MIT License
