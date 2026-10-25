# schema_events.py

def create_events_table(conn):
    # Drop events and dependent schema objects, including referencing foreign keys.
    drop_events_table = "DROP TABLE IF EXISTS events CASCADE;"

    # Define events with foreign keys to users and venues.
    create_events_table = """--sql
                CREATE TABLE events (
                    event_id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description VARCHAR(255),
                    starts_at TIMESTAMPTZ NOT NULL,
                    ends_at TIMESTAMPTZ NOT NULL,
                    organiser_id INT REFERENCES users(user_id),
                    venue_id INT REFERENCES venues(venue_id),
                    created_at TIMESTAMPTZ DEFAULT NOW()
                );"""

    # Create a cursor using the supplied connection.
    cursor = conn.cursor()

    # Drop the events table if it exists.
    cursor.execute(drop_events_table)
    print("DROP TABLE completed.")

    # Create events; the referenced users and venues tables must already exist.
    cursor.execute(create_events_table)
    print("CREATE TABLE completed.")

    # Save the transaction's changes.
    conn.commit()

    # Release the cursor; the connection remains open.
    cursor.close()