import pytest
import requests

from src.config.constants import BASE_URL, AUTH_HEADERS, AUTH_DATA, API_HEADERS
from faker import Faker

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    response = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert response.status_code == 200, f"Auth failed: {response.status_code}, {response.text}"

    token = response.json().get("access_token")
    assert token, "No access_token found"

    session.headers.update(API_HEADERS)
    session.headers.update({"Authorization": f"Bearer {token}"})

    return session


@pytest.fixture()
def item_data():
    return {
        "title": faker.word().capitalize(),
        "description": faker.sentence(nb_words=10)
    }


@pytest.fixture()
def limit_number():
    return faker.random_int(min=1, max=20)


@pytest.fixture()
def data_too_long():
    return {
        "title": faker.text(max_nb_chars=356),
        "description": faker.text(max_nb_chars=356)
    }
