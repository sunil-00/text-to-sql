from fastapi import FastAPI


app = FastAPI(title="Text-to-SQL App", description="Convert Natural Language to SQL")

@app.get("/")
def home():
    return {"message": "Welcome to Text-to-SQL API"}
