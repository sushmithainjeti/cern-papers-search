from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator
import httpx
import re

app = FastAPI()

Instrumentator().instrument(app).expose(app)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

INSPIRE_API = "https://inspirehep.net/api/literature"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"papers": [], "query": "", "sort": "mostrecent"})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = "", sort: str = "mostrecent"):
    papers = []
    if q:
        async with httpx.AsyncClient() as client:
            response = await client.get(INSPIRE_API, params={
                "sort": sort,
                "size": 25,
                "q": q,
                "fields": "titles,authors,abstracts,arxiv_eprints,publication_info,earliest_date"
            })
            data = response.json()
            for hit in data.get("hits", {}).get("hits", []):
                meta = hit.get("metadata", {})

                arxiv = meta.get("arxiv_eprints", [{}])[0].get("value", "")
                link = f"https://arxiv.org/abs/{arxiv}" if arxiv else ""

                year = ""
                pub_info = meta.get("publication_info", [])
                if pub_info and pub_info[0].get("year"):
                    year = str(pub_info[0].get("year"))
                elif meta.get("earliest_date"):
                    year = meta.get("earliest_date", "")[:4]

                if not year:
                    year = "N/A"

                raw_abstract = meta.get("abstracts", [{}])[0].get("value", "No abstract available")
                clean_abstract = re.sub(r'<[^>]+>', '', raw_abstract)

                papers.append({
                    "title": meta.get("titles", [{}])[0].get("title", "No title"),
                    "authors": [a.get("full_name", "") for a in meta.get("authors", [])[:3]],
                    "abstract": clean_abstract,
                    "year": year,
                    "link": link,
                })

    return templates.TemplateResponse(request, "index.html", {"papers": papers, "query": q, "sort": sort})
