###--------------IMPORTS--------------###
import sys

sys.path.insert(0,"/home/suleyman/projects/northcoders/2projects/nc-plus-one")

from fastapi import status
from fastapi.testclient import TestClient
from rich.pretty import pprint

###-----------------------------------###

# ----------- #
# -- TESTS -- #
# ----------- #

def test_create_user_returns_expected_status_and_initial_structure(client: TestClient, user_valid_dict) -> None:
    """Expected Result: Dictionary with one key-value pair / Status Code 200
    {
        'user_id': 8, 
        'username': 'jigglejeben', 
        'email': 'logical@example.com', 
        'password': '676767676767676767676767676767', 
        'created_at': '2026-10-30T12:45:06.419377+01:00'
    }
    """
    response = client.post(
        "/users",
        json=user_valid_dict,
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.headers["content-type"] == "application/json"
    assert list(response.json()) == ['user']
    
    
def test_create_user_returns_expected_structure(client: TestClient, user_valid_dict) -> None:
    """Expected Structure: Dictionary with 5 key-value pairs"""
    response = client.post(
        "/users",
        json=user_valid_dict,
    ).json()["user"]
    assert list(response.keys()) == ['user_id', 'username', 'email', 'password', 'created_at']
    assert isinstance(response, dict)
    
    
def test_create_user_returns_expected_content(client: TestClient, user_valid_dict) -> None:
    """Expected Content: Three fixed and two auto created fields"""
    response = client.post(
        "/users",
        json=user_valid_dict,
    ).json()["user"]
    assert isinstance(response["username"], str)
    assert isinstance(response["email"], str)
    assert isinstance(response["password"], str)
    assert response["username"] == "jigglejeben"
    assert response["email"] == "logical@example.com"
    assert response["password"] == "676767676767676767676767676767"
    
def test_create_user_with_duplicate_email_returns_409(client: TestClient, users_duplicate_email) -> None:
    response = client.post(
        "/users",
        json=users_duplicate_email,
    )
    pprint(response)



# TODO: Create test data that takes random limited test data to test.
    # - How it would work: 
    #   - It would look into the .json data files extract a limited number of rows, 
    #       either first row or randomly. Could also test all data, but with real live 
    #       data this may become unfeasible.

# TODO: Basic Error Testing
    #   - Valid User
    #   - Status code errors
    #   - Emails should be unique. Gives Error.
    #   - Missing or Invalid fields


# POSSIBLE IMPLEMENTATIONS
# TODOFUTURE: Add testing for empty users
# TODOFUTURE: Add more data to use, allow loading of json without causing
#               issues with RAM.
# TODOFUTURE: Duplicate emails cause 500 Internal Server Error, but no explicit 
    #           409 Conflict Error. Only message below in terminal: 
    #   psycopg.errors.UniqueViolation: duplicate key value violates unique constraint "users_email_key"
    #   DETAIL:  Key (email)=(chacna@example.com) already exists.