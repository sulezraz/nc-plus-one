import os
from pathlib import Path

import psycopg  # Connects Python to PostgreSQL
from dotenv import load_dotenv  # Loads settings from an environment file


def get_connection() -> psycopg.Connection:
    """Load environment settings and return a PostgreSQL connection."""
    # Read the ENV environment setting; use "development" if it is not set.
    ENV = os.getenv("ENV", "development")
    
    # Find the project root: the folder containing the db directory.
    project_root = Path(__file__).resolve().parents[1]
    # Load the selected environment file from that root.
    env_file = project_root / f".env.{ENV}"
    load_dotenv(env_file)
    
    database = os.getenv("PGDATABASE") # Read the database name from the environment.
    
    if not database:    # CHECK: Stop if the database name is missing or empty.
        raise RuntimeError("PGDATABASE NOT SET")
    print(f"Database configured: {database}")
    
    # OPEN CONNECTION using standard PostgreSQL environment settings.
    connection = psycopg.connect()  # Psycopg reads PGDATABASE automatically
    print(f"Connected to {database}")

    return connection



