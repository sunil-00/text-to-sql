import re


def sanitize_sql_query(query: str) -> str:
    """
    Sanitize the SQL query by:
    1. Removing comments (single-line and multi-line).
    2. Removing unnecessary whitespace and excessive spaces (while keeping newlines).
    3. Removing unnecessary characters (like backticks and quotes).
    4. Keeping newlines intact.
    """
    # Step 1: Remove single-line comments (everything after --)
    query = re.sub(r"--.*", "", query)
    
    # Step 2: Remove multi-line comments (everything between /* and */)
    query = re.sub(r"/\*.*?\*/", "", query, flags=re.DOTALL)
    
    # Step 3: Remove unnecessary backticks (if any)
    query = re.sub(r"`", "", query)

    # Step 4: Normalize spaces but keep newlines
    # First, replace multiple spaces and tabs with a single space
    query = re.sub(r"[ \t]+", " ", query)
    
    # Step 5: Remove spaces that are next to newlines (preserve newlines)
    query = re.sub(r"\s*\n\s*", "\n", query)  # Remove leading/trailing spaces around newlines

    # Step 6: Normalize single quotes if needed (optional)
    query = re.sub(r"\'", "'", query)  # Normalize single quotes if needed

    # Step 7: Trim the final query to remove leading/trailing spaces
    query = query.strip()

    return query


def is_valid_sql(sql_query: str) -> bool:
    """
    Validates the SQL query to prevent SQL injection and restrict dangerous operations.
    :param sql_query: The SQL query to validate.
    :return: True if the query is valid, False otherwise.
    """
    sql_query = sql_query.lower()

    # List of prohibited SQL commands to prevent unsafe operations.
    prohibited_keywords = ['insert', 'delete', 'update', 'drop', 'truncate', 'alter', 'create']

    if any(keyword in sql_query for keyword in prohibited_keywords):
        return False

    # Check for common SQL injection patterns.
    injection_patterns = [r"--", r"or\s+1=1"]
    if any(re.search(pattern, sql_query) for pattern in injection_patterns):
        return False

    return True
