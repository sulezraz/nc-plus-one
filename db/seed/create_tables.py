# db/seed/create_tables.py
# Creates the users, venues, events and rsvps tables with their columns, constraints and default values.


def create_users_table(conn):
    # Define the user columns, constraints and generated defaults.
    create_users_sql = """--sql
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            user_password VARCHAR(255) NOT NULL,
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    """

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(create_users_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    print("CREATE TABLE users.")


def create_venues_table(conn):
    # Define the venue columns; address and capacity may be NULL.
    create_venues_sql = """--sql
        CREATE TABLE venues (
            venue_id SERIAL PRIMARY KEY,
            venue_name VARCHAR(255) NOT NULL,
            address TEXT,
            capacity INT
        );
    """

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(create_venues_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    print("CREATE TABLE venues.")


def create_events_table(conn):
    # Define events with foreign keys to users and venues.
    create_events_sql = """--sql
        CREATE TABLE events (
            event_id SERIAL PRIMARY KEY,
            event_name VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            starts_at TIMESTAMPTZ NOT NULL,
            ends_at TIMESTAMPTZ NOT NULL,
            organiser_id INT REFERENCES users(user_id),
            venue_id INT REFERENCES venues(venue_id),
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    """

    # The referenced users and venues tables must already exist.
    with conn.cursor() as cursor:
        cursor.execute(create_events_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    print("CREATE TABLE events.")


def create_rsvps_table(conn):
    # Define RSVPs with foreign keys to users and events.
    create_rsvps_sql = """--sql
        CREATE TABLE rsvps (
            rsvp_id SERIAL PRIMARY KEY,
            attendee_id INT REFERENCES users(user_id),
            event_id INT REFERENCES events(event_id),
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
    """

    # The referenced users and events tables must already exist.
    with conn.cursor() as cursor:
        cursor.execute(create_rsvps_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    print("CREATE TABLE rsvps.")