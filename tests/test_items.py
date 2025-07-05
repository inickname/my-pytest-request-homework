import requests

from src.config.constants import BASE_URL, API_HEADERS


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"
    empty_item_data = {"title": "", "description": None}

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        TestItems.created_item_id = item_id

    def test_create_item_without_token(self, item_data):
        response = requests.post(self.endpoint, json=item_data, headers=API_HEADERS)
        assert response.status_code == 401, f"Response: {response.status_code}, {response.text}"

    def test_create_item_with_erroneous_data(self, auth_session):
        response = auth_session.post(self.endpoint, json=self.empty_item_data)
        assert response.status_code == 422, f"Response: {response.status_code}, {response.text}"

    def test_create_item_with_data_too_long(self, auth_session, data_too_long):
        response = auth_session.post(self.endpoint, json=data_too_long)
        assert response.status_code == 422, f"Response: {response.status_code}, {response.text}"

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)

        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

    def test_get_limited_items(self, auth_session, limit_number):
        response = auth_session.get(f"{self.endpoint}?limit={limit_number}")
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert len(data["data"]) == limit_number

    def test_get_item_filtered_by_id(self, auth_session):
        response = auth_session.get(f"{self.endpoint}{self.created_item_id}")
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert not "data" in data, "Response is not filtered"
        assert isinstance(data, object), "'data' is not a object"
        assert data.get("id") == self.created_item_id

    def test_get_item_without_token(self):
        response = requests.get(f"{self.endpoint}{self.created_item_id}", headers=API_HEADERS)
        assert response.status_code == 401, f"Response: {response.status_code}, {response.text}"

    def test_update_item(self, item_data, auth_session):
        response = auth_session.put(f"{self.endpoint}{self.created_item_id}", json=item_data)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("title") == item_data["title"]
        assert data.get("description") == item_data["description"]

    def test_update_item_with_erroneous_data(self, auth_session):
        response = auth_session.put(f"{self.endpoint}{self.created_item_id}", json=self.empty_item_data)
        assert response.status_code == 422, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data['detail'][0].get("msg") == "String should have at least 1 character", \
            f"Response message: {data['detail'][0]['msg']}"

    def test_update_item_with_data_too_long(self, auth_session, data_too_long):
        response = auth_session.put(f"{self.endpoint}{self.created_item_id}", json=data_too_long)
        assert response.status_code == 422, f"Response: {response.status_code}, {response.text}"

    def test_update_non_existent_item(self, auth_session, item_data):
        response = auth_session.put(f"{self.endpoint}non-existent-id", json=item_data)
        assert response.status_code == 422, f"Response: {response.status_code}, {response.text}"

    def test_delete_item_without_token(self):
        response = requests.delete(f"{self.endpoint}{self.created_item_id}", headers=API_HEADERS)
        assert response.status_code == 401, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("detail") == "Not authenticated", f"Response message: {data['detail'][0]['msg']}"

    def test_delete_item(self, auth_session):
        response = auth_session.delete(f"{self.endpoint}{self.created_item_id}")
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("message") == "Item deleted successfully", f"Response message: {data['message']}"

        get_deleted_booking = auth_session.get(f"{self.endpoint}{self.created_item_id}")
        assert get_deleted_booking.status_code == 404, "Item was not deleted"

    def test_delete_item_second_time(self, auth_session):
        response = auth_session.delete(f"{self.endpoint}{self.created_item_id}")
        assert response.status_code == 404, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("detail") == "Item not found", f"Response message: {data['detail'][0]['msg']}"
