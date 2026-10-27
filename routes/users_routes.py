from fastapi import APIRouter

from db.connection import get_connection

users_router = APIRouter(prefix="/users")

##### GET ALL USERS #####
@users_router.get("/")
def get_all_users():

    # Open a database connection and create a cursor for executing SQL.
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
                SELECT * FROM users
                ORDER BY username,
                        user_id;
                """)

    # CHECK: SELECT provides column metadata, even when no rows match.
    assert cur.description is not None

    # Extract column names from the query metadata.
        # ["user_id", "username", "email", "user_password", "created_at"]
    columns = [desc[0] for desc in cur.description]

    # Retrieve all rows as a list of tuples, or [] if the table is empty.
        # [(1, 'Alice Rahman', 'alice@example.com', 'password123', ...),
        #  (2, 'Bob Nguyen', 'bob@example.com', 'password123', ...),
        #  ...]
    rows = cur.fetchall()

    # Empty list does not raise an error as this may be a intended behaviour
    if not rows:
        print("TERRIFYING: No users have been found.")

    # Close the cursor, then close the database connection.
    cur.close()
    conn.close()

    # Pair column names with values to create a list of user dictionaries.
        # [{'user_id': 1, 'username': 'Alice Rahman', ...},
        #  {'user_id': 2, 'username': 'Bob Nguyen', ...},
        #  ...]
    users = [dict(zip(columns, row)) 
            for row in rows]

    # Return the user dictionaries inside a response dictionary.
        # {'users': [{'user_id': 1, 'username': 'Alice Rahman', ...},
        #            {'user_id': 2, 'username': 'Bob Nguyen', ...},
        #            ...]}
    # If there are no users: {'users': []}
    return {"users": users}
