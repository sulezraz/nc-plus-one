import os
from pathlib import Path

import psycopg  # Connects Python to PostgreSQL
from dotenv import load_dotenv  # Loads settings from an environment file


def get_connection() -> psycopg.Connection:
    
    # READ SETTINGS FROM .env FILE
    # Read the ENV environment setting; use "development" if it is not set.
    ENV = os.getenv("ENV", "development")
    
    # Find the project root: the folder containing the db directory.
    project_root = Path(__file__).resolve().parents[1]
    # Load the selected environment file from that root.
    env_file = project_root / f".env.{ENV}"
    load_dotenv(env_file)
    
    # Read the database name from the environment.
    database = os.getenv("PGDATABASE")
    
    # CHECK: Stop if the database name is missing or empty.
    if not database:
        raise RuntimeError("PGDATABASE NOT SET")
    print(f"Database configured: {database}")
    
    # OPEN CONNECTION using standard PostgreSQL environment settings.
    # Psycopg reads PGDATABASE automatically
    connection = psycopg.connect()
    print(f"Connected to {database}")

    return connection


