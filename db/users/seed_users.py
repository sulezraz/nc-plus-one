# seed_users.py
from db.load_json import convert_tuple, load_json


def insert_users_table(conn):
    # Load users.json and convert each record into a tuple.
    users = convert_tuple(load_json("users.json"))

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Insert each tuple in name, email, password order.
    cursor.executemany(
        """--sql
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