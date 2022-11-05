from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), "static")
templantes = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request, usuario: str = "Alexandre Santos"):
    context = {
        "request": request,
        "usuario": usuario
    }
    
    return templantes.TemplateResponse('index.html', context=context)

@app.get("/servicos")
async def servicos(request: Request):
    context = {"request": request}
    return templantes.TemplateResponse('servicos.html', context=context)