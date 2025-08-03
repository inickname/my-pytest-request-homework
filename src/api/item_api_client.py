from src.enums.enums import Url


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = Url.BASE_URL.value

    def get_items(self, item_id=""):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/api/v1/items/{item_id}")
        if response.status_code != 200:
            response.raise_for_status()
        return response

    def create_item(self, item_data):
        """Отправляет запрос на создание item."""
        response = self.auth_session.post(f"{self.base_url}/api/v1/items/", json=item_data.model_dump())
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status()  # Выбросит HTTPError для плохих статусов
        return response
