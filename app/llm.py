from groq import Groq

from app.config import GROQ_API_KEY, MODEL


client = Groq(
    api_key=GROQ_API_KEY,
)

chat_history = []


def add_to_chat_history(role: str, content: str) -> None:
    chat_history.append({'role': role, 'content': content})


def get_llm_response(query: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            messages=chat_history,
            model=MODEL,
        )
        llm_response = chat_completion.choices[0].message.content
        add_to_chat_history('user', query)
        add_to_chat_history('assistant', llm_response)
    except Exception:
        return "Oops! Something went wrong. Please try again."

    return llm_response
