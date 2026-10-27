# /reset_and_seed_database.py
# Recreates the application tables and populates them with initial JSON seed data.


from db.connection import get_connection
from db.seed.create_tables import (
    create_events_table,
    create_rsvps_table,
    create_users_table,
    create_venues_table,
)
from db.seed.drop_tables import (
    drop_events_table,
    drop_rsvps_table,
    drop_users_table,
    drop_venues_table,
)
from db.seed.seed_tables import (
    insert_events_table,
    insert_rsvps_table,
    insert_users_table,
    insert_venues_table,
)

conn = get_connection()

def seed():
    ##### DROP TABLES #####
    drop_users_table(conn)
    drop_venues_table(conn)    
    drop_events_table(conn) # Create events after the users and venues tables it references.
    drop_rsvps_table(conn)  # Create RSVPs after the users and events tables it references.
    print()


    ##### CREATE TABLES #####
    create_users_table(conn)
    create_venues_table(conn)
    create_events_table(conn) # Create events after the users and venues tables it references.
    create_rsvps_table(conn)  # Create RSVPs after the users and events tables it references.
    print()


    ##### INSERT INITIAL DATA #####
    # Insert users and venues before events that reference their IDs.
    insert_users_table(conn)
    insert_venues_table(conn)
    insert_events_table(conn)
    insert_rsvps_table(conn) # Insert RSVPs after the users and events they reference.
    print()


if __name__ == "__main__":
    seed()



# TODO: Build data-transformation utilities using TDD.

