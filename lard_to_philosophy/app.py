import os.path
import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from mangum import Mangum

app = FastAPI()
template_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "templates")
templates = Jinja2Templates(directory=template_dir)


@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/hello", status_code=200)
def hello():
    return "Hello World"


handler = Mangum(app)
