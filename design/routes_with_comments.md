# `users_routes.py`

Defines user endpoints, such as `GET /users/`, and the functions that handle their requests.

## Full Code Block
```python
# users_routes.py
# Defines users endpoints, such as GET /users/, and the functions
# that handle their requests.

from fastapi import APIRouter, HTTPException

from db.connection import get_connection

users_router = APIRouter(prefix="/users")


##################################################
#                     GET                        #
##################################################

########## RETURNS A LIST OF USERS ##########
# Default: Ordered by username, then user_id.

@users_router.get("/")
def get_all_users():
    # Open a database connection and create a cursor for executing SQL.
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""--sql
        SELECT *
        FROM users
        ORDER BY username, user_id;
    """)

    # CHECK: SELECT provides column metadata, even when no rows match.
    assert cur.description is not None

    # Extract column names from the query metadata.
    # ["user_id", "username", "email", "password", "created_at"]
    columns = [desc[0] for desc in cur.description]

    # Retrieve all rows as a list of tuples, or [] if the table is empty.
    # [(1, 'Alice Rahman', 'alice@example.com', 'password123', ...),
    #  (2, 'Bob Nguyen', 'bob@example.com', 'password123', ...),
    #  ...]
    rows = cur.fetchall()

    # Close the cursor, then close the database connection.
    cur.close()
    conn.close()

    # An empty list does not raise an error because it may be intended.
    if not rows:
        print("TERRIFYING: No users have been found.")

    # Pair column names with values to create a list of user dictionaries.
    # [{'user_id': 1, 'username': 'Alice Rahman', ...},
    #  {'user_id': 2, 'username': 'Bob Nguyen', ...},
    #  ...]
    users = [
        dict(zip(columns, row))
        for row in rows
    ]

    # Return the user dictionaries inside a response dictionary.
    # {'users': [{'user_id': 1, 'username': 'Alice Rahman', ...},
    #            {'user_id': 2, 'username': 'Bob Nguyen', ...},
    #            ...]}
    # If there are no users: {'users': []}
    return {"users": users}


########## RETURNS A SINGLE USER BY ID ##########

@users_router.get("/{user_id}")
def get_users_member(user_id: int):
    # FastAPI validates and converts the URL parameter to an integer.

    # Open a database connection and create a cursor.
    conn = get_connection()
    cur = conn.cursor()

    # Select the user whose ID matches the supplied user_id.
    # Psycopg uses the value supplied in (user_id,) for the %s placeholder.

    # First argument: the SQL instructions.
    query = """
        SELECT *
        FROM users
        WHERE user_id = %s
    """

    # Second argument: the values for the placeholders.
    parameters = (user_id,)  # For example, (3,) if user_id is 3.

    # Pass both arguments to the function.
    cur.execute(query, parameters)

    columns = [desc[0] for desc in cur.description]  # type: ignore

    # Retrieve the matching row as a tuple, or None if not found.
    row = cur.fetchone()

    cur.close()
    conn.close()

    # CHECK: Return a 404 error if no matching user exists.
    if row is None:
        raise HTTPException(status_code=404, detail="Member not found")

    # Convert the matching row into a dictionary for FastAPI's JSON response.
    user = dict(zip(columns, row))

    return {"user": user}

```

## GET endpoints

### Return a list of users

**Endpoint:** `GET /users/`

Returns all users ordered by `username`, then `user_id`.

#### Open the database connection
Create a cursor for executing SQL.
```python
@users_router.get("/")
def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
```

#### Execute the query
```python
    cur.execute("""
        SELECT *
        FROM users
        ORDER BY username, user_id;
    """)
```

#### Extract column names
`SELECT` provides column metadata even when no rows match.
```python
    assert cur.description is not None

    columns = [desc[0] for desc in cur.description]
```

Example column names:
```python
["user_id", "username", "email", "password", "created_at"]
```

#### Retrieve the rows
Retrieve all rows as a list of tuples, or `[]` if the table is empty.
```python
    rows = cur.fetchall()
```

Example rows:
```python
[
    (1, "Alice Rahman", "alice@example.com", "password123", ...),
    (2, "Bob Nguyen", "bob@example.com", "password123", ...),
    ...
]
```

#### Close the connection
Close the cursor, then the database connection.
```python
    cur.close()
    conn.close()
```

#### Handle an empty result
An empty list does not raise an error because it may be intended behaviour.
```python
    if not rows:
        print("TERRIFYING: No users have been found.")
```

#### Convert rows into dictionaries
Pair column names with values to create a list of user dictionaries.
```python
    users = [
        dict(zip(columns, row))
        for row in rows
    ]
```

Example result:
```python
[
    {"user_id": 1, "username": "Alice Rahman", ...},
    {"user_id": 2, "username": "Bob Nguyen", ...},
    ...
]
```

#### Return the response
Return the user dictionaries inside a response dictionary.
```python
    return {"users": users}
```

Example response structure:
```python
{
    "users": [
        {"user_id": 1, "username": "Alice Rahman", ...},
        {"user_id": 2, "username": "Bob Nguyen", ...},
        ...
    ]
}
```

If there are no users:
```json
{"users": []}
```

### Return a single user by ID

**Endpoint:** `GET /users/{user_id}`

FastAPI validates and converts the URL parameter to an integer.

#### Open the database connection
```python
@users_router.get("/{user_id}")
def get_users_member(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
```

#### Prepare and execute the query
Select the user whose `user_id` matches the supplied value.

Psycopg uses the values passed separately in `parameters` for the `%s` placeholders.
```python
    query = """
        SELECT *
        FROM users
        WHERE user_id = %s
    """

    parameters = (user_id,)

    cur.execute(query, parameters)
```

The two arguments to `cur.execute()` are:
- `query`: the SQL instructions.
- `parameters`: the values for the placeholders—for example, `(3,)` when `user_id` is `3`.

#### Extract column names and retrieve the row
`fetchone()` returns the matching row as a tuple, or `None` if no user is found.
```python
    columns = [desc[0] for desc in cur.description]  # type: ignore
    row = cur.fetchone()
```

#### Close the connection
```python
    cur.close()
    conn.close()
```

#### Handle a missing user
Raise an HTTP `404` error if no matching row exists.
```python
    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )
```

#### Return the response
Convert the matching row into a dictionary for FastAPI’s JSON response.
```python
    user = dict(zip(columns, row))

    return {"user": user}
```

