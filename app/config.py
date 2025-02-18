import os

from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")

assert GROQ_API_KEY, "GROQ_API_KEY is not set"
assert MODEL, "MODEL is not set"
