# seed_venues.py
from db.load_json import convert_tuple, load_json


def insert_venues_table(conn):
    # Load venues.json and convert each record into a tuple.
    venues = convert_tuple(load_json("venues.json"))

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Insert each tuple in name, address, capacity order.
    cursor.executemany(
        """--sql
        INSERT INTO venues (name, address, capacity)
        VALUES (%s, %s, %s);
        """,
        venues,
    )
    print("INSERT complete.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()