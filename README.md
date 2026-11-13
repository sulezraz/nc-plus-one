# NC Plus One

## Contents
- [Overview](#overview)
- [What it enables](#what-it-enables)
- [Data stored](#data-stored)
  - [Database relationships](#database-relationships)
- [Backend scope](#backend-scope)
- [Technologies used](#technologies-used)
- [Project structure](#project-structure)
- [Installation](#installation)
  - [Part 1: Setup](#part-1-setup)
    - [1. Fork and clone](#1-fork-and-clone)
    - [2. Set up with Make](#2-set-up-with-make)
    - [3. Configure the database connection](#3-configure-the-database-connection)
  - [Part 2: Create and seed the database](#part-2-create-and-seed-the-database)
    - [Start PostgreSQL](#start-postgresql)
    - [Create the database](#create-the-database)
    - [Seed data](#seed-data)
    - [Verify the seed data](#verify-the-seed-data)
  - [Part 3: Start the server](#part-3-start-the-server)
- [Testing](#testing)
  - [Test database setup](#test-database-setup)
  - [Run tests](#run-tests)

## Overview

NC Plus One is a **REST API** that provides the **backend for an events platform**.

The project includes:
- **PostgreSQL database integration** to store and retrieve application data.
- An **automated test suite** to verify API behaviour, database operations and data-transformation utilities.

The API is designed to support a future frontend application.

## What it enables

The API helps users **find and attend events** and enables organisers to **create events and manage registrations**.

### Feature scope

The features below describe the API’s intended scope.

| Role | Features |
|---|---|
| **Users / attendees** | Create an account and log in |
| | Browse events and view their details |
| | RSVP to an event |
| | View and cancel their registrations |
| **Organisers** | Create and update their events |
| | See who has registered |
| | View audience statistics for their events |
## Data stored
- **Users:** people using the platform.
- **Venues:** places where events happen.
- **Events:** activities people can attend.
- **RSVPs:** registrations connecting users to events.

### Database relationships

The database contains **four tables**: three main tables (`users`, `venues` and `events`) and one linking table (`rsvps`).
- `events.organiser_id` references `users.user_id`, identifying the event's organiser.
- `events.venue_id` references `venues.venue_id`, identifying where the event takes place.
- `rsvps.attendee_id` references `users.user_id`, identifying the attendee.
- `rsvps.event_id` references `events.event_id`, identifying the event they registered for.

The `rsvps` table connects users to events: a user can register for multiple events, and an event can have multiple attendees.

## Backend scope

### Architecture

The REST API sits between clients and the PostgreSQL database:
```text
Client / frontend ⇄ REST API ⇄ PostgreSQL database
```

#### Local request flow
```text
Browser / frontend / HTTP client
        ↓ HTTP request
Uvicorn → FastAPI endpoint
        ↓
Database connection using settings from .env.development
        ↓ Psycopg sends a SQL query
Local PostgreSQL database
        ↓ Query results
FastAPI prepares a JSON response
        ↓
Client receives the response
```

### Components and responsibilities

#### REST API
- **What it does:** Handles client requests through endpoints and returns structured JSON with appropriate status codes and consistent error responses.
- **Responsibilities:** Validates input, protects data integrity, manages authentication and enforces application rules and permissions.

#### PostgreSQL database
- Stores application data in tables, using **relationships and constraints** to maintain data integrity.
- Seed data provides initial records for development and testing.

#### Database integration
- Uses **Psycopg** to connect to PostgreSQL and execute queries that read and change database records.

#### Test suite
- Uses **integration tests** to verify endpoints and their database interactions.
- Uses **unit tests** to verify data-transformation utilities.

## Technologies used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **FastAPI** | API endpoints and request handling |
| **Uvicorn** | Server that runs the FastAPI application |
| **Pydantic** | Request validation and structured data models |
| **PostgreSQL** | Relational database for application data |
| **Psycopg 3** | Python connections and queries to PostgreSQL |
| **pytest** | Automated tests and reusable test fixtures |
| **TestClient** | Sends requests directly to the application during API tests |
| **python-dotenv** | Loads local configuration from environment files |
## Project structure

### Application and database
- `main.py`: Creates the FastAPI application and registers the routers.
- `routes/`: Defines API endpoints and their request handlers.
- `models/pydantic_models.py`: Defines models for validating request data.
- `db/connection.py`: Loads environment settings and opens PostgreSQL connections.
- `db/create_database.sql`: Deletes and recreates the database for initial setup.
- `db/load_json.py`: Loads JSON seed data and converts records into tuples.
- `db/data/`: Contains the initial JSON seed records.
- `db/seed/create_tables.py`: Creates the application tables.
- `db/seed/drop_tables.py`: Drops the application tables.
- `db/seed/seed_tables.py`: Inserts the seed records.
- `reset_and_seed_database.py`: Coordinates dropping, creating and seeding tables.

### Testing and manual requests
- `tests/`: Contains automated tests.
- `tests/conftest.py`: Selects the test environment before application imports and can provide shared test fixtures.
- `pytest.toml`: Configures test discovery and output. Currently enables strict checks, verbose results, long tracebacks, local variable details and live print output.
- `requests.http`: Stores example HTTP requests for manual endpoint checks using a compatible client or editor extension.

### Project configuration
- `Makefile`: Provides commands to create the virtual environment, install dependencies and run development checks.
- `requirements.txt`: Lists the Python dependencies and their pinned versions, grouped by purpose.
- `pyproject.toml`: Defines package metadata and setuptools build settings; currently includes `db` and its subpackages.
- `.gitignore`: Lists local environment files, virtual environments and caches that Git should ignore.

### Documentation
- `README.md`: Explains the project and how to set up, run and test it.
- `NOTES.md`: Stores helpful development commands.
- `TODO.md`: Tracks planned features and implementation tasks.

## Installation

These setup instructions assume Ubuntu or Ubuntu running in WSL. After cloning, run project commands from the `nc-plus-one` folder.

### Part 1: Setup

#### 1. Fork and clone
Open [sulezraz/nc-plus-one](https://github.com/sulezraz/nc-plus-one) and select **Fork** to create a copy under your GitHub account.

Clone your fork, replacing `YOUR_USERNAME` with your GitHub username:
```bash
git clone https://github.com/YOUR_USERNAME/nc-plus-one.git
cd nc-plus-one
```

#### 2. Set up with Make
Run these **from the project's root directory**, in this order:
```bash
make requirements # Create .venv and install the packages in requirements.txt
make dev-setup    # Install Bandit, Black and pytest-cov for development checks
make run-checks   # Run the enabled checks (currently Bandit security scanning)
```

The Make commands activate `.venv` for their own commands. Before running the manual Python commands in the following steps, activate it in your terminal:
```bash
source .venv/bin/activate
```

#### 3. Configure the database connection
Create `.env.development` in the project root:
```dotenv
PGDATABASE=nc_plus_one
```

If your PostgreSQL setup requires them, add the relevant connection settings:
```dotenv
PGUSER=your_postgres_user
PGPASSWORD=your_postgres_password
PGHOST=localhost
PGPORT=5432
```

Replace the example values with your local settings. Psycopg reads these `PG...` variables automatically. Without `ENV` set, the connection code loads `.env.development`.

Keep files containing credentials out of Git. The repository ignores `.env.*` files.

### Part 2: Create and seed the database

#### Start PostgreSQL
For Ubuntu/WSL with PostgreSQL installed locally, start the database service:
```bash
sudo service postgresql start
```
Enter your Ubuntu/WSL password if prompted. No characters will appear as you type—this is normal.

Check that it is accepting connections:
```bash
pg_isready
```

PostgreSQL must be running before creating databases, seeding data, using database-backed endpoints or running integration tests. If it is already running, there is no need to start it again.

#### Create the database
Create the development database once:
```bash
createdb nc_plus_one
```
If it already exists, this reports an error without changing it.

Optional - For a specific PostgreSQL role or host, use:
```bash
createdb -U your_postgres_user -h localhost nc_plus_one
```
`createdb` does not load `.env.development`.

Alternatively, run the database creation script:
```bash
psql -d postgres -f db/create_database.sql
```
**Warning:** this script deletes and recreates the database if it already exists.

#### Seed data
Create the tables and insert the initial JSON data:
```bash
python -m reset_and_seed_database
```

**Reseeding deletes and recreates the application tables and their data.** Use it for development resets; the database itself does not need recreating.

#### Verify the seed data
Check the connected database and role, display up to ten users, and count the user records:
```bash
psql -d nc_plus_one \
  -c "SELECT current_database(), current_user;" \
  -c "SELECT user_id, username, email, created_at FROM users ORDER BY user_id LIMIT 10;" \
  -c "SELECT COUNT(*) AS total_rows FROM users;"
```

The displayed columns exclude passwords. Add `-U` and `-h` options if required; `psql` does not load `.env.development` automatically.

### Part 3: Start the server
```bash
python -m uvicorn main:app --reload
```
Keep this terminal running while using the API. Press `Ctrl+C` to stop the server.

Open the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Testing

`make run-tests` runs the tests, but PostgreSQL and the test database must be ready first. Complete the setup below once unless your Make target already handles it.

### Test database setup

With PostgreSQL running, create a separate test database once:
```bash
createdb nc_plus_one_test
```

Use the same PostgreSQL role and host options as in Part 2 if required.

Create `.env.test` in the project root:
```dotenv
PGDATABASE=nc_plus_one_test
```

Add any required `PGUSER`, `PGPASSWORD`, `PGHOST` and `PGPORT` settings for the test database. Keep this file out of Git.

`tests/conftest.py` selects the test environment and database before importing application or seed code. pytest loads this configuration automatically. Test fixtures should reset and seed the test database before tests that require predictable data.

### Run tests

From the project's root directory:
```bash
make run-tests # Run the test suite using the Makefile target
```

**PostgreSQL must be running. Uvicorn is not required** for FastAPI `TestClient` tests.
