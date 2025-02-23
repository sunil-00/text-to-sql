import os

from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")

assert GROQ_API_KEY, "GROQ_API_KEY is not set"
assert MODEL, "MODEL is not set"

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

assert DATABASE_HOST, "DATABASE_HOST is not set"
assert DATABASE_PORT, "DATABASE_PORT is not set"
assert DATABASE_NAME, "DATABASE_NAME is not set"
assert DATABASE_USER, "DATABASE_USER is not set"
assert DATABASE_PASSWORD, "DATABASE_PASSWORD is not set"
