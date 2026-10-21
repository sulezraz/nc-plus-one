from connection import get_connection
from schema import create_users_table
from seed import insert_users_table

# Open a connection and create the users table.
create_users_table(get_connection())
print()

# Open another connection and insert the users.
insert_users_table(get_connection())