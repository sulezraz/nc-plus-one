# db/seed/drop_tables.py
# Drops the users, venues, events and rsvps tables and their dependent schema objects.
import psycopg


def drop_users_table(conn: psycopg.Connection) -> None:
    # CASCADE also removes dependent objects, including referencing foreign keys.
    drop_users_sql = "DROP TABLE IF EXISTS users CASCADE;"

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(drop_users_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("DROP TABLE users.")


def drop_venues_table(conn: psycopg.Connection) -> None:
    # CASCADE also removes dependent objects, including referencing foreign keys.
    drop_venues_sql = "DROP TABLE IF EXISTS venues CASCADE;"

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(drop_venues_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("DROP TABLE venues.")


def drop_events_table(conn: psycopg.Connection) -> None:
    # CASCADE also removes dependent objects, including referencing foreign keys.
    drop_events_sql = "DROP TABLE IF EXISTS events CASCADE;"

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(drop_events_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("DROP TABLE events.")


def drop_rsvps_table(conn: psycopg.Connection) -> None:
    # CASCADE also removes dependent objects, including referencing foreign keys.
    drop_rsvps_sql = "DROP TABLE IF EXISTS rsvps CASCADE;"

    # Execute the statement and automatically close the cursor.
    with conn.cursor() as cursor:
        cursor.execute(drop_rsvps_sql)

    # Commit before reporting success; the connection remains open.
    conn.commit()
    # print("DROP TABLE rsvps.")