from fastapi import FastAPI

from app.llm import get_llm_response


app = FastAPI(title="Text-to-SQL App", description="Convert Natural Language to SQL")


@app.get("/")
def home():
    return {"message": "Welcome to Text-to-SQL API"}


@app.post("/query")
def query(query: str):
    response = get_llm_response(query)
    return {"message": response}
