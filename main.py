from fastapi import FastAPI

app = FastAPI()


@app.get("/api/")
def index() -> dict:
    return {"status": "ok"}


@app.get("/")
def index_web():
    return ('<h1>Hello World</h1>')
