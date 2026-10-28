# users_routes.py
# Defines users endpoints, such as GET /users/, and the functions that handle their requests.

from fastapi import APIRouter, HTTPException

from db.connection import get_connection

users_router = APIRouter(prefix="/users")


# -- GET -- # 

# - Return a list of users - #
@users_router.get("/")
def get_all_users():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
        SELECT *
        FROM users
        ORDER BY username, user_id;
    """)

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()

    cur.close()
    conn.close()

    if not rows:
        print("TERRIFYING: No users have been found.")

    # Map database columns to row values; an empty result returns [].
    users = [dict(zip(columns, row)) for row in rows]
    return {"users": users}


# - Returns a single user by ID - #
@users_router.get("/{user_id}")
def get_users_member(user_id: int):
    conn = get_connection()
    cur = conn.cursor()

    query = """--sql
        SELECT *
        FROM users
        WHERE user_id = %s;  -- Keep only rows where user_id = the supplied parameter value.
    """

    # Pass values separately so the driver handles SQL parameters safely.
    cur.execute(query, (user_id,))

    assert cur.description is not None
    columns = [desc[0] for desc in cur.description]
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Member not found. Are you sure they're real.")

    user = dict(zip(columns, row))
    return {"user": user}


# TODO: Create a user (POST).
# TODO: Change a user's password (PATCH).
# TODO: Delete a user (DELETE).