# api.py -> main.py later
# python -m uvicorn api.py:app --reload

from fastapi import FastAPI, HTTPException

from db.connection import get_connection

app = FastAPI(title="NC Plus One")

@app.get("/users")
def get_all_users():
    conn = get_connection()
    cur = conn.cursor()  # A cursor executes SQL and retrieves results.

    # Order by username
    cur.execute("""--sql
                SELECT * FROM users
                ORDER BY username, user_id;
                """)

    # CHECK: SELECT should provide column metadata.
    assert cur.description is not None

    # Extract column names from the query metadata: ["id", "name", ...].
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()  # Retrieve all matching rows as a list of tuples.

    # No returned row means the mission ID did not match.
    if rows is None:
        raise HTTPException(status_code=404, detail="TERRIFYING: No users have been found.",)

    # Release the database resources after fetching the data.
    cur.close()
    conn.close()

    # Pair column names with values to create one dictionary per row.
    bare_dictionary = [dict(zip(columns, row)) for row in rows]

    return {"users": bare_dictionary} # RETURNS: single dictionary with one key value pair