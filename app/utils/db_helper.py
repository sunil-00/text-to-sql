import psycopg2
from typing import Dict, List

from app.config import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_NAME
)


def get_db_connection(database_url: str):
    """
    Establishes and returns a connection to the PostgreSQL database.
    """
    try:
        if database_url:
            return psycopg2.connect(database_url)
        
        return psycopg2.connect(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME,
        )
    except psycopg2.Error as e:
        raise Exception(f"Error connecting to the database: {e}")


def get_db_schema(database_url: str = None) -> Dict[str, List[Dict[str, str]]]:
    """
    Fetches the schema of all tables in the PostgreSQL database.
    :param database_url (Optional): The connection string to the PostgreSQL database.
    :return: Dictionary with table names as keys and lists of column metadata.
    """
    conn = None
    try:
        conn = get_db_connection(database_url)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()

        schema = {}
        for table in tables:
            table_name = table[0]
            cursor.execute("""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = %s
            """, (table_name,))
            columns = cursor.fetchall()
            schema[table_name] = [{"column": col[0], "type": col[1]} for col in columns]

        cursor.close()
        conn.close()
        return schema
    except Exception as e:
        raise Exception(f"Error fetching schema: {e}")
    finally:
        if conn is not None:
            conn.close()


def execute_sql_query(sql_query: str, database_url: str = None) -> Dict:
    """
    Executes a validated SQL query and returns the results.
    :param sql_query: The SQL query to execute.
    :param database_url (Optional): The connection string to the PostgreSQL database.
    :return: A dictionary with columns and rows of the result.
    """
    conn = None
    try:
        conn = get_db_connection(database_url)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()

        return {"columns": columns, "rows": rows, "query": sql_query, "empty": len(rows) == 0}
    except psycopg2.Error as e:
        raise Exception(f"Error executing query: {e}")
    finally:
        if conn is not None:
            conn.close()
