import os

import psycopg  # Connects Python to PostgreSQL
from dotenv import load_dotenv  # Loads settings from an environment file


def get_connection():
    
    # READ SETTINGS FROM .env FILE
    # Read the ENV environment setting; use "development" if it is not set.
    ENV = os.getenv("ENV", "development")
    # Load database settings for the selected environment.
    load_dotenv(f".env.{ENV}")
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
