from constants import BASE_URL


class TestItems:
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (200, 201), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        TestItems.created_item_id = item_id

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

    def test_update_item(self, item_data, auth_session):
        response = auth_session.put(f"{self.endpoint}{self.created_item_id}", json=item_data)
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("title") == item_data["title"]
        assert data.get("description") == item_data["description"]

    def test_delete_item(self, auth_session):
        response = auth_session.delete(f"{self.endpoint}{self.created_item_id}")
        assert response.status_code == 200, f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert data.get("message") == "Item deleted successfully", f"Response message: {data['message']}"

        get_deleted_booking = auth_session.get(f"{self.endpoint}{self.created_item_id}")
        assert get_deleted_booking.status_code == 404, "Item was not deleted"
