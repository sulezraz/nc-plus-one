###--------------IMPORTS--------------###
import sys

sys.path.insert(0,"/home/suleyman/projects/northcoders/2projects/nc-plus-one")

from fastapi import status
from fastapi.testclient import TestClient
from rich.pretty import pprint

###-----------------------------------###

# TODO: Make 404 tests

# # ----------- #
# # -- TESTS -- #
# # ----------- #

# # -- GET -- #
# def test_GET_users_returns_with_status_200_and_json_content(client: TestClient) -> None:
#     # Send GET /users and check for a successful response.
#     users = client.get("/users")
#     assert users.status_code == status.HTTP_200_OK
#     assert users.headers["content-type"] == "application/json"

# def test_GET_users_returns_expected_user_structure(client):
#     # Parse the response body and extract the value under "users".
#     users = client.get("/users").json()["users"]
#     assert list(users[0].keys()) == ['user_id', 'username', 'email', 'password', 'created_at']
#     assert isinstance(users, list)
#     assert isinstance(users[0], dict)

# def test_GET_events_returns_with_status_200_and_json_content(client: TestClient) -> None:
#     events = client.get("/events")
#     assert events.status_code == status.HTTP_200_OK
#     assert events.headers["content-type"] == "application/json"

# def test_GET_events_returns_expected_events_structure(client):
#     events = client.get("/events").json()["events"]
#     assert list(events[0].keys()) == ['event_id', 'event_name', 'description', 'starts_at', 'ends_at', 'organiser_id', 'venue_id', 'created_at']
#     assert isinstance(events, list)
#     assert isinstance(events[0], dict)

# def test_GET_venues_returns_with_status_200_and_json_content(client: TestClient) -> None:
#     venues = client.get("/venues")
#     assert venues.status_code == status.HTTP_200_OK
#     assert venues.headers["content-type"] == "application/json"

# def test_GET_venues_returns_expected_venues_structure(client):
#     venues = client.get("/venues").json()["venues"]
#     assert list(venues[0].keys()) == ['venue_id', 'venue_name', 'address', 'capacity']
#     assert isinstance(venues, list)
#     assert isinstance(venues[0], dict)
    
# def test_GET_rsvps_returns_with_status_200_and_json_content(client: TestClient) -> None:
#     rsvps = client.get("/rsvps")
#     assert rsvps.status_code == status.HTTP_200_OK
#     assert rsvps.headers["content-type"] == "application/json"

# def test_GET_rsvps_returns_expected_rsvps_structure(client):
#     rsvps = client.get("/rsvps").json()["rsvps"]
#     assert list(rsvps[0].keys()) == ['rsvp_id', 'attendee_id', 'event_id', 'created_at']
#     assert isinstance(rsvps, list)
#     assert isinstance(rsvps[0], dict)


# # TODO: Make tests for GET single IDs


# # -- POST -- #



