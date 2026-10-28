# Project Overview

Based on the file tree and code shared, these are the main groups. Descriptions of files whose contents have not been reviewed are based on their usual purpose.

## 1. FastAPI application

These files handle incoming requests and outgoing responses.

| File                        | What it does                                                                                                                        |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `main.py`                   | Creates the FastAPI application and registers your routers. <br>Uvicorn starts the application defined here.                        |
| `routes/users_routes.py`    | Defines users endpoints, such as `GET /users/`, <br>and the functions that handle their requests.                                   |
| `models/pydantic_models.py` | Defines Pydantic models describing expected data fields and types, <br>usually for validating request bodies or defining responses. |

## 2. Database configuration and initial setup

These select the database, connect to it and perform initial database setup.

| File               | What it does                                                                                             |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| `.env.development` | Holds development settings, such as `PGDATABASE`, and <br>any required username, password, host or port. |
| `db/connection.py` | Loads connection settings and provides `get_connection()` <br>to open a PostgreSQL connection.           |
| `db/setup.sql`     | Contains database setup commands. These drop and recreate the database itself.                           |

**Database setup and table resets are separate operations.** Normally, run the setup SQL initially, then use the reset script for later development resets.

## 3. Table creation, resetting and seeding

These rebuild your tables and populate them with starting data.

| File | What it does |
|---|---|
| `reset_and_seed_database.py` | Coordinates the complete reset: calls the drop functions, create functions and insert functions in order. |
| `db/seed/drop_tables.py` | Defines functions that drop the application tables and their dependent schema objects. |
| `db/seed/create_tables.py` | Defines functions that create tables, columns, constraints, foreign keys and defaults. |
| `db/seed/seed_tables.py` | Loads the starting records and inserts them into the corresponding tables. |
| `db/load_json.py` | Provides the JSON-loading and tuple-conversion helpers used by the seed functions. |

## 4. Initial JSON data

These hold the records inserted during seeding.

| File | What it contains |
|---|---|
| `db/data/users.json` | Starting user records. |
| `db/data/venues.json` | Starting venue records. |
| `db/data/events.json` | Starting event records, including references to users and venues. |
| `db/data/rsvps.json` | Starting RSVP records connecting attendees to events. |

The JSON files contain **data**; the Python seed functions contain the **instructions for inserting it**.

## 5. Testing and manually checking requests

| File | What it does |
|---|---|
| `tests/test_api.py` | Contains automated tests, presumably focused on API requests, responses and status codes. |
| `tests/test_app.py` | Contains additional application tests; the exact distinction from `test_api.py` depends on its contents. |
| `pytest.toml` | Configures pytest—for example, test locations and default command options. This filename is supported from **pytest 9.0**. |
| `requests.http` | Stores HTTP requests you can send manually using a compatible editor extension or HTTP client. |

Pytest reads `pytest.toml` as a **configuration file**; it does not contain the test functions themselves.

## 6. Python project and dependencies

| File | What it does |
|---|---|
| `pyproject.toml` | Defines Python project metadata, build/package settings and potentially dependencies or tool configuration. |
| `requirements.txt` | Lists packages to install with `python -m pip install -r requirements.txt`, possibly with version restrictions. |

These can overlap: whether dependencies belong in one or both depends on how the project is configured.

## 7. Editor, formatting and Git settings

| File | What it does |
|---|---|
| `.vscode/launch.json` | Defines VS Code debugging configurations: what to launch and how to launch it. |
| `.vscode/settings.json` | Stores VS Code settings specific to this workspace, such as formatters or editor behaviour. |
| `.sqlfluff` | Configures SQLFluff’s SQL dialect, formatting and linting rules. |
| `.gitignore` | Lists untracked files and folders Git should ignore, such as credentials, virtual environments and generated files. |

## 8. Documentation

| File | What it does |
|---|---|
| `README.md` | Explains the project, installation, setup, seeding, server startup and testing instructions. |
| `structure.txt` | Stores a text snapshot of the project’s folder/file layout. It becomes outdated when the structure changes unless regenerated. |

## 9. Generated package metadata

The `nc_plus_one.egg-info/` directory contains metadata generated by Python packaging tools.

| File | What it does |
|---|---|
| `PKG-INFO` | Records package information such as its name, version and description. |
| `SOURCES.txt` | Lists source files selected for packaging. |
| `dependency_links.txt` | Records legacy dependency-link information; it may be empty. |
| `top_level.txt` | Lists the top-level Python modules or packages provided by the project. |

**These files are normally generated rather than edited manually.** They describe the Python package, not the PostgreSQL database or its records.