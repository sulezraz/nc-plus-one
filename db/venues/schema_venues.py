# schema_venues.py

def create_venues_table(conn):
    # Drop venues and dependent schema objects, including referencing foreign keys.
    drop_venues_table = "DROP TABLE IF EXISTS venues CASCADE;"

    # Define the venue columns; address and capacity may be NULL.
    create_venues_table = """--sql
                CREATE TABLE venues (
                    venue_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    address TEXT,
                    capacity INT
                );"""

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Execute the drop statement, skipping a missing table.
    cursor.execute(drop_venues_table)
    print("DROP TABLE completed.")

    # Create the venues table.
    cursor.execute(create_venues_table)
    print("CREATE TABLE completed.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()