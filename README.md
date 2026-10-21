# 🎟️ NC Plus One

## CONTENTS
- PART 1 - OVERVIEW
- PART 2 - Create and connect to a database by running setup.sql
- PART 3 - ERD (Entity Relationship Diagram)
- PART 4 - CONFIGURE ENV
- PART 5 - File Structure


### PART 1 - OVERVIEW
NC Plus One is a backend project for an events platform. Its goal is to build a REST API that allows users to discover events, RSVP and manage their attendance, while giving organisers tools to create events and understand their audience.

### Planned features
#### Attendees
- Register an account.
- Browse available events.
- RSVP to events.
- Manage their attendance.

#### Organisers
- Create and manage events.
- View audience and attendance statistics.

### Architecture
The API forms the backend layer of a full stack application:

```text
Client / frontend ⇄ REST API ⇄ Database
```

It will receive HTTP requests, apply business logic, communicate with the database and return structured JSON responses. Authentication, data integrity and application rules are central responsibilities of the API.

A frontend is outside this project's scope. The API will be designed with frontend developers in mind, using clear endpoints, predictable responses and appropriate HTTP status codes.

### Engineering approach
- **Version control:** regular commits with clear, descriptive messages.
- **Configuration:** environment variables for credentials and settings, with local secrets excluded from Git.
- **Testing:** integration tests for each endpoint's successful behaviour and documented error cases, plus unit tests for data transformation utilities.
- **Error handling:** consistent error responses and appropriate HTTP status codes.
- **Documentation:** setup instructions and API usage examples added as the implementation develops.

### PART 2 - Create and connect to a database by running setup.sql

**RUN FILE**
```bash
psql -d postgres -f db/setup.sql
```

You should see if database does not exist:
```text
psql:db/setup.sql:2: NOTICE:  database "nc_plus_one" does not exist, skipping DROP DATABASE
CREATE DATABASE
You are now connected to database "nc_plus_one" as user "your_name".
```

OR you should see if database does exist:
```text
DROP DATABASE
CREATE DATABASE
You are now connected to database "nc_plus_one" as user "your_name".
```

### PART 3 - ERD (Entity Relationship Diagram)

**4 tables:**
- **3 main tables:** Users, Venues, Events
  - `users.user_id = events.organiser_id`
  - `venues.venue_id = events.venue_id`
- **1 linking table:** RSVPs — connects Users and Events
  - `users.user_id = rsvps.attendee_id`
  - `events.event_id = rsvps.event_id`


### PART 4 - CONFIGURE ENV

- Create a .env.development file in the project root and set PGDATABASE=nc_plus_one. 
- Add your local PostgreSQL username, password, host and port if your setup requires them. 
- Keep this file out of Git.

### PART 5 - File Structure
- main.py - runs main functions: create_users_table, insert_users_table
- connection.py - Open a connection using standard PostgreSQL environment settings
- load_json.py
- schema.py
- seed.py


### PART 5 - Quick INSERT check

- Check data has been inserted into users
  ```bash
  psql -d nc_plus_one -c "SELECT current_database(), current_user;" -c "SELECT * FROM users LIMIT 10;" -c "SELECT COUNT(*) AS total_rows FROM users;"
  ```

