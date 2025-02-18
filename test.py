from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/{chemin}", response_class=HTMLResponse)
async def home(request: Request, chemin: str):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "message": f"Bienvenue sur FastAPI avec SSR {chemin}!",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
