from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static", html = True), name="static")

@app.get("/")
async def main():
    with open("./static/index.html") as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html", status_code=200)