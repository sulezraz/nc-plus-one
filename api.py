# api.py
from fastapi import FastAPI

from db.connection import get_connection

app = FastAPI(title="NC Plus One")

@app.get("/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor()  # A cursor executes SQL and retrieves results.

    cur.execute("SELECT * FROM users")

    # Extract column names from the query metadata: ["id", "name", ...].
    columns = [desc[0] for desc in cur.description]  # type: ignore
    rows = cur.fetchall()  # Retrieve all matching rows as a list of tuples.

    # Release the database resources after fetching the data.
    cur.close()
    conn.close()

    # Pair column names with values to create one dictionary per row.
    return [dict(zip(columns, row)) for row in rows]