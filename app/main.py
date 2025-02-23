from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.llm import get_llm_response, chat_history


app = FastAPI(title="Text-to-SQL App", description="Convert Natural Language to SQL")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home():
    return {"message": "Welcome to Text-to-SQL API"}


@app.post("/query")
def query(request: Request, query: str = Form(...)):
    llm_response = get_llm_response(query.strip())
    return templates.TemplateResponse("llm_response.html", {"request": request, "llm_response": llm_response})


@app.get("/chat")
def chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": chat_history})


@app.delete("/chat")
def delete_chat(request: Request):
    chat_history.clear()
    return templates.TemplateResponse("messages.html", {"request": request, "chat_history": chat_history})


@app.get("/clear-chat-modal")
async def clear_chat_modal(request: Request):
    return templates.TemplateResponse("modal.html", {"request": request})
