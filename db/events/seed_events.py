# seed_events.py
from db.load_json import convert_tuple, load_json


def insert_events_table(conn):
    # Load events.json and convert each record into a tuple.
    events = convert_tuple(load_json("events.json"))

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Insert each event tuple in the column order listed below.
    cursor.executemany(
        """--sql
        INSERT INTO events (title, description, starts_at, ends_at, organiser_id, venue_id)
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        events,
    )
    print("INSERT complete.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()