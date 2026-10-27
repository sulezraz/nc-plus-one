import os

import pytest

from reset_and_seed_database import seed

os.environ["ENV"] = "test"

@pytest.fixture(autouse=True)
def seed_test_db():
    
    seed()
    

@pytest.fixture()
def client():
    return TestClient(app)


def test_get_plants_responds_with200(client):
    response = client.get("/plants")

    assert response.status_code == 200


def test_get_plants_responds_with_list_on_key_of_plants(client):
    plants = client.get("/plants").json()["plants"]

    assert isinstance(plants, list)
