from db.connection import get_connection
from db.events.schema_events import create_events_table
from db.events.seed_events import insert_events_table
from db.rsvps.schema_rsvps import create_rsvps_table
from db.rsvps.seed_rsvps import insert_rsvps_table
from db.users.schema_users import create_users_table
from db.users.seed_users import insert_users_table
from db.venues.schema_venues import create_venues_table
from db.venues.seed_venues import insert_venues_table

# RESET TABLES
# Each schema helper drops and recreates its table.

create_users_table(get_connection())
print()

create_venues_table(get_connection())
print()

# Create events after the users and venues tables it references.
create_events_table(get_connection())
print()

# Create RSVPs after the users and events tables it references.
create_rsvps_table(get_connection())
print()


# INSERT INITIAL DATA
# Insert users and venues before events that reference their IDs.

insert_users_table(get_connection())
print()

insert_venues_table(get_connection())
print()

insert_events_table(get_connection())
print()

# Insert RSVPs after the users and events they reference.
insert_rsvps_table(get_connection())
print()


# TODO: Separate dropping and creating into focused functions.
# TODO: Build data-transformation utilities using TDD.

