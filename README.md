# CERN Papers Search Engine

A full-stack search engine for high energy physics research papers, built on top of CERN's official Inspire-HEP API.

## Features
- Real-time search across millions of CERN research papers
- Sort by Most Recent or Most Cited
- Click any paper to open the full PDF on arXiv
- Clean, responsive UI

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Search Engine | OpenSearch |
| Frontend | Jinja2, HTML, CSS |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Data Source | Inspire-HEP API |

## Run Locally

\`\`\`bash
git clone https://github.com/sushmithainjeti/cern-papers-search.git
cd cern-papers-search
docker-compose up --build
\`\`\`

Open http://localhost:8000

## Author
📧 sushmithainjeti529@gmail.com
