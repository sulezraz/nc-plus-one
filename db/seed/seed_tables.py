# db/seed/seed_tables.py
# Inserts JSON seed data into the users, venues, events and rsvps tables.

import psycopg

from db.load_json import convert_tuple, load_json


def insert_users_table(conn: psycopg.Connection) -> None:
    # Load users.json and convert each record into a tuple.
    users = convert_tuple(load_json("users.json"))

    # Insert tuples in username, email, password order.
    with conn.cursor() as cursor:
        cursor.executemany(
            """--sql
            INSERT INTO users (
                username,
                email,
                password)
            VALUES (%s, %s, %s);
            """,
            users,
        )

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("INSERT INTO users committed.")


def insert_venues_table(conn: psycopg.Connection) -> None:
    # Load venues.json and convert each record into a tuple.
    venues = convert_tuple(load_json("venues.json"))

    # Insert tuples in name, address, capacity order.
    with conn.cursor() as cursor:
        cursor.executemany(
            """--sql
            INSERT INTO venues (
                venue_name,
                address,
                capacity)
            VALUES (%s, %s, %s);
            """,
            venues,
        )

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("INSERT INTO venues committed.")


def insert_events_table(conn: psycopg.Connection) -> None:
    # Load events.json and convert each record into a tuple.
    events = convert_tuple(load_json("events.json"))

    # Insert event tuples in the column order listed below.
    with conn.cursor() as cursor:
        cursor.executemany(
            """--sql
            INSERT INTO events (
                event_name,
                description,
                starts_at,
                ends_at,
                organiser_id,
                venue_id
            )
            VALUES (%s, %s, %s, %s, %s, %s);
            """,
            events,
        )

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("INSERT INTO events committed.")


def insert_rsvps_table(conn: psycopg.Connection) -> None:
    # Load rsvps.json and convert each record into a tuple.
    rsvps = convert_tuple(load_json("rsvps.json"))

    # Insert RSVP tuples in attendee_id, event_id order.
    with conn.cursor() as cursor:
        cursor.executemany(
            """--sql
            INSERT INTO rsvps (
                attendee_id,
                event_id)
            VALUES (%s, %s);
            """,
            rsvps,
        )

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("INSERT INTO rsvps committed.")