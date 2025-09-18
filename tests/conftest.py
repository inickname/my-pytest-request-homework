import pytest
import requests

from src.enums.urls import Url
from src.enums.headers import Headers
from src.enums.data import AuthData
from faker import Faker

from src.data_models.item_request_data_model import ItemDataModel

faker = Faker()

BASE_URL = Url.BASE_URL.value
AUTH_HEADERS = Headers.AUTH_HEADERS.value
AUTH_DATA = AuthData.AUTH_DATA.value
API_HEADERS = Headers.API_HEADERS.value


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
    def _item_data():
        item = ItemDataModel.create_item_data()
        return item

    yield _item_data


@pytest.fixture()
def data_too_long():
    def _data_too_long():
        data_too_long = ItemDataModel.creating_too_long_data()
        return data_too_long

    yield _data_too_long

# @pytest.fixture()
# def limit_number():
#     return faker.random_int(min=1, max=20)
