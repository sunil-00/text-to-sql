from typing import Dict, List


def format_schema_for_llm(schema: Dict[str, List[Dict[str, str]]]) -> str:
    """
    Formats the schema into a readable string format for LLM.
    :param schema: The database schema (tables and columns).
    :return: Formatted schema string for LLM.
    """
    schema_str = ""
    for table, columns in schema.items():
        schema_str += f"Table: {table}\n"
        for column in columns:
            schema_str += f"  - {column['column']} ({column['type']})\n"
        schema_str += "\n"
    return schema_str


def create_llm_system_prompt(schema_str: str) -> str:
    """
    Creates a system prompt to send to the LLM API.
    :param schema_str: The formatted schema string.
    :return: system prompt string.
    """
    return f"""
You are a powerful language model that generates SQL queries for a PostgreSQL database.
The following is the schema of the database:

{schema_str}

Please generate a valid SQL query for the given user query using the above schema.
The SQL should be valid for PostgreSQL.
Do not include any explanations, clarifications, or extra information. Just provide the SQL query in response to the input request.
"""
