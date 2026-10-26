# schema_users.py

def create_users_table(conn):
    # Drop users and dependent schema objects, including referencing foreign keys.
    drop_users_table = "DROP TABLE IF EXISTS users CASCADE;"

    # Define the user columns, constraints and generated defaults.
    create_users_table = """--sql
                CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    user_password VARCHAR(255) NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );"""

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Execute the drop statement, skipping a missing table.
    cursor.execute(drop_users_table)
    print("DROP TABLE completed.")

    # Create the users table.
    cursor.execute(create_users_table)
    print("CREATE TABLE completed.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()