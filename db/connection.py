"""Read the database settings from an environment file and use Psycopg to connect Python to PostgreSQL."""

import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv


def get_connection() -> psycopg.Connection:
    # Default to development; tests/conftest.py sets ENV to "test".
    ENV = os.getenv("ENV", "development")

    # Load .env.development or .env.test from the project root.
    project_root = Path(__file__).resolve().parents[1]
    env_file = project_root / f".env.{ENV}"
    load_dotenv(env_file)

    database = os.getenv("PGDATABASE")

    # Stop if the database name is missing or empty.
    if not database:
        raise RuntimeError("PGDATABASE NOT SET")
    print(f"Database configured: {database}")

    # Psycopg reads PGDATABASE and other PostgreSQL environment settings automatically.
    connection = psycopg.connect()
    print(f"Connected to {database}")

    return connection