# users_routes.py
# Defines users endpoints, such as GET /users/, and the functions that handle their requests.
import sys

sys.path.insert(0,"/home/suleyman/projects/northcoders/2projects/nc-plus-one")

from fastapi import APIRouter, HTTPException
from psycopg.errors import UniqueViolation
from rich.pretty import pprint

from db.connection import get_connection
from models.pydantic_models import UserCreate, UserUpdate

users_router = APIRouter(prefix="/users")


#-----------#
# -- GET -- # 
#-----------#

# -- Return a list of users
#       Order by username ASC -- #
@users_router.get("/")
def get_all_users() -> dict[str, list[dict]]:
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


# -- Returns a single user by ID -- #
@users_router.get("/{user_id}")
def get_user(user_id: int) -> dict[str, dict[str, int]]:
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


#------------#
# -- POST -- # 
#------------#

# -- Add a new user -- #
@users_router.post("/", status_code=201)
def create_user(user: UserCreate) -> dict[str, dict]:
    """Create and return a user, raising HTTP 409 if a unique value (email) already exists."""
    conn = get_connection()
    cur = conn.cursor()

    query = """--sql
        INSERT INTO users (
            username,
            email,
            password
        )
        VALUES (%s, %s, %s)
        RETURNING *;
    """

    try:
        # Pass values separately so the driver handles SQL parameters safely.
        cur.execute(
            query,
            (
                user.username,
                user.email,
                user.password,
            ),
        )

        # Read column names and the inserted row returned by RETURNING *.
        assert cur.description is not None
        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()

        conn.commit()  # Save the new user.

        assert row is not None
        # Pair column names with their values to build the response.
        posted_user = dict(zip(columns, row))
        return {"user": posted_user}

    except UniqueViolation as e:
        # Show database error details in the server terminal.
        print()
        print("Constraint failed:", e.diag.constraint_name)
        print("Conflict details:", e.diag.message_detail)
        print()

        # Return a conflict response to the client, preserving the original cause.
        raise HTTPException(
            status_code=409,
            detail={
                "Severity": e.diag.severity,
                "Code Error": "409 Conflict",
                "Message": e.diag.message_primary,
                "Detail": e.diag.message_detail,
                "Table/Field": e.diag.constraint_name,

}

            
        ) from e

    finally:
        # Release database resources whether the operation succeeds or fails.
        cur.close()
        conn.close()

    







# # -- MANUAL RESPONSE INSPECTION -- #
# if __name__ == "__main__":
#     pprint("ALL USERS:")
#     pprint(get_all_users())
#     print()

#     pprint("SINGLE USER:")
#     pprint(get_user(1))  # Use a user ID that exists.