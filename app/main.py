from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.llm import (
    chat_history,
    generate_sql_from_llm,
    add_to_chat_history
)
from app.utils import (
    get_db_schema,
    format_schema_for_llm,
    create_llm_system_prompt,
    execute_sql_query,
    sanitize_sql_query,
    is_valid_sql
)

app = FastAPI(title="Text-to-SQL App", description="Convert Natural Language to SQL")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home():
    return {"message": "Welcome to Text-to-SQL API"}


def send_llm_response(request: Request, content: dict):
    add_to_chat_history('assistant', content)
    return templates.TemplateResponse("llm_response.html", {"request": request, "llm_response": content})


def handle_error(request: Request, message: str):
    return send_llm_response(request, {'error': True, 'content': message})


@app.post("/query")
def query(request: Request, query: str = Form(...)):
    query = query.strip()
    add_to_chat_history('user', query)
    
    try:
        schema = get_db_schema()
        formatted_schema = format_schema_for_llm(schema)
        llm_system_prompt = create_llm_system_prompt(formatted_schema)
        llm_response = generate_sql_from_llm(query, llm_system_prompt)
    except Exception:
        return handle_error(request, "Oops! Something went wrong. Please try again.")

    llm_response = sanitize_sql_query(llm_response)

    if not is_valid_sql(llm_response):
        return handle_error(request, "The LLM response is not a valid SQL query.")

    try:
        results = execute_sql_query(llm_response)
        return send_llm_response(request, results)
    except Exception as e:
        return handle_error(request, f"Error executing SQL query: {e}")


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
