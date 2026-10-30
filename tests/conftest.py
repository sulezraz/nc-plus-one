"""Provide test fixtures for database seeding, API clients, and user input data."""

import pytest
from fastapi.testclient import TestClient

from main import app
from reset_and_seed_database import seed


# -------------- #
# -- FIXTURES -- #
# -------------- #
@pytest.fixture(autouse=True)
def seed_test_db() -> None:
    # Reset and seed the configured database before each test in this file.
    seed()

@pytest.fixture()
def client() -> TestClient:
    # Create a fresh test client for each test that requests it.
    return TestClient(app)

# -------------- #


# -- DATA -- #

@pytest.fixture
def user_valid_dict():
    return {
        "username": "jigglejeben",
        "email": "logical@example.com",
        "password": "676767676767676767676767676767",
    }


@pytest.fixture
def users_duplicate_email():
    return {
        "username": "Suleyman Rasul",
        "email": "chacna@example.com",
        "password": "password123"
    }