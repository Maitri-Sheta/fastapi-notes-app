from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
conn = MongoClient("mongodb+srv://db_user:db_user@database.nyahjtx.mongodb.net/notes")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", "Untitled Note"),
            "desc": doc.get("desc", doc.get("note", ""))
        })

    return templates.TemplateResponse(
       request=request,
       name="index.html",
       context={"newDocs": newDocs}
    )

@app.post("/")
async def add_note(title: str = Form(...), desc: str = Form(...)):
    note_item = {
        "title": title,
        "desc": desc
    }
    conn.notes.notes.insert_one(note_item)
    return RedirectResponse(url="/", status_code=303)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
