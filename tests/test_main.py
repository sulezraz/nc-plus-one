import pytest
from fastapi import status
from fastapi.testclient import TestClient
from rich.pretty import pprint

from main import app
from reset_and_seed_database import seed


@pytest.fixture(autouse=True)
def seed_test_db():
    # Reset and seed the configured database before each test in this file.
    seed()


@pytest.fixture()
def client():
    # Create a fresh test client for each test that requests it.
    return TestClient(app)


def test_GET_users_responds_with_status_200(client):
    # Send GET /users and check for a successful response.
    users = client.get("/users")

    assert users.status_code == status.HTTP_200_OK
    assert users.headers["content-type"] == "application/json"

def test_GET_users_responds_with_list_on_key_of_users(client):
    # Parse the response body and extract the value under "users".
    users = client.get("/users").json()["users"]
    
    assert list(users[0].keys()) == ['user_id', 'username', 'email', 'user_password', 'created_at']
    assert isinstance(users, list)
    assert isinstance(users[0], dict)
    
    
    
    
    
    
    
    
    
    
    
    








    # assert response.json() == {
    #         "users": [
    #             {
    #             "user_id": 1,
    #             "username": "Alice Rahman",
    #             "email": "alice@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             },
    #             {
    #             "user_id": 2,
    #             "username": "Bob Nguyen",
    #             "email": "bob@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             },
    #             {
    #             "user_id": 3,
    #             "username": "Carol Singh",
    #             "email": "carol@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             },
    #             {
    #             "user_id": 4,
    #             "username": "David Okafor",
    #             "email": "david@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             },
    #             {
    #             "user_id": 5,
    #             "username": "Eve Martinez",
    #             "email": "eve@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             },
    #             {
    #             "user_id": 6,
    #             "username": "Frank Liu",
    #             "email": "frank@example.com",
    #             "user_password": "password123",
    #             "created_at": "2026-10-26T08:20:45.081994+01:00"
    #             }
    #         ]
    #         }
        
