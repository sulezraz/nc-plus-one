from fastapi import status
from fastapi.testclient import TestClient

from api import app

client = TestClient(app)

def test_GET_request_returns_correct_responses_and_correct_data_in_order():
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "users": [
            {
            "user_id": 1,
            "username": "Alice Rahman",
            "email": "alice@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            },
            {
            "user_id": 2,
            "username": "Bob Nguyen",
            "email": "bob@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            },
            {
            "user_id": 3,
            "username": "Carol Singh",
            "email": "carol@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            },
            {
            "user_id": 4,
            "username": "David Okafor",
            "email": "david@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            },
            {
            "user_id": 5,
            "username": "Eve Martinez",
            "email": "eve@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            },
            {
            "user_id": 6,
            "username": "Frank Liu",
            "email": "frank@example.com",
            "user_password": "password123",
            "created_at": "2026-10-26T08:20:45.081994+01:00"
            }
        ]
        }