# seed.py
from load_json import convert_tuple, load_json


def insert_users_table(conn):
    # Load the JSON records and convert them into tuples.
    users = convert_tuple(load_json())

    # Create a cursor to execute SQL.
    cursor = conn.cursor()

    # Insert each tuple in name, email, password order.
    cursor.executemany(
        """
        INSERT INTO users (name, email, password)
        VALUES (%s, %s, %s);
        """,
        users,
    )
    print("INSERT complete.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()
