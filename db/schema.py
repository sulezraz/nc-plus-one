# schema.py

def create_users_table(conn):
    
    # SQL statements to reset the users table.
    drop_users_table = "DROP TABLE IF EXISTS users;"
    create_users_table = """
                CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );"""

    # Create a cursor to execute SQL.
    cursor = conn.cursor()

    # Drop the users table if it exists.
    cursor.execute(drop_users_table)
    print("DROP TABLE completed.")

    # Recreate the users table with its columns and constraints.
    cursor.execute(create_users_table)
    print("CREATE TABLE completed.")

    # Save the transaction's changes.
    conn.commit()
    # Release the cursor; the connection remains open.
    cursor.close()
