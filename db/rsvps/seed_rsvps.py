# seed_rsvps.py
from db.load_json import convert_tuple, load_json


def insert_rsvps_table(conn):
    # Load rsvps.json and convert each record into a tuple.
    rsvps = convert_tuple(load_json("rsvps.json"))

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Insert each event tuple in the column order listed below.
    cursor.executemany(
        """--sql
        INSERT INTO rsvps (attendee_id, event_id)
        VALUES (%s, %s);
        """,
        rsvps,
    )
    print("INSERT complete.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()