import os

import psycopg  # Connects Python to PostgreSQL
from dotenv import load_dotenv  # Loads settings from an environment file


def get_connection():
    
    ENV = os.getenv("ENV", "development")  # Default to development if ENV is unset.

    # Load database settings for the selected environment.
    load_dotenv(f".env.{ENV}")

    # Stop if the database name is missing or empty.
    if not os.getenv("PGDATABASE"):
        raise RuntimeError("PGDATABASE NOT SET")
    
    # Read the database name from the environment.
    database = os.getenv("PGDATABASE")
    print(f"Database configured: {database}")
    
    # Open a connection using standard PostgreSQL environment settings.
    # Psycopg reads PGDATABASE automatically
    connection = psycopg.connect()
    print("Connected to database")

    return connection