from os.path import isfile
from mimetypes import guess_type
from fastapi import FastAPI, Response, Request, templating
t = templating.Jinja2Templates(directory="./htmlcov")

app = FastAPI()

@app.get("/")
def get_root(request: Request):
    return t.TemplateResponse("index.html", {"request": request})

@app.get("/{filename}")
async def get_site(filename):
    filename = './htmlcov/' + filename

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename, mode="r", errors="ignore") as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)