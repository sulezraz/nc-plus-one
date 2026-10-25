# schema_rsvps.py

def create_rsvps_table(conn):
    # Drop rsvps and dependent schema objects, including referencing foreign keys.
    drop_rsvps_table = "DROP TABLE IF EXISTS rsvps CASCADE;"


    create_rsvps_table = """--sql
                CREATE TABLE rsvps (
                    rsvp_id SERIAL PRIMARY KEY,
                    attendee_id INT REFERENCES users(user_id),
                    event_id INT REFERENCES events(event_id),
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );"""

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Execute the drop statement, skipping a missing table.
    cursor.execute(drop_rsvps_table)
    print("DROP TABLE completed.")

    # Create rsvps; the referenced users and venues tables must already exist.
    cursor.execute(create_rsvps_table)
    print("CREATE TABLE completed.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()