from src.api.item_api_client import ItemApiClient
from src.data_models.item_response_data_model import ItemResponseModel
from src.utils.validate_item_response import ValidateItemResponse


class ItemScenarios:
    def __init__(self, api_client: ItemApiClient):  # Типизация для ясности
        self.api_client = api_client

    def get_and_verify_items_exist(self):
        """
        Сценарий: получить список items и проверить, что он не пуст.
        """
        items = self.api_client.get_items().json()
        assert len(items) > 0, "Список items пуст"
        print(f"Получено {len(items)} items id.")
        return items

    def create_item_check_and_delete(self, item_data):
        """
        Сценарий: создать booking и сразу же его удалить.
        Возвращает ID созданного и удаленного booking.
        """
        item_data = item_data()
        created_item_data = self.api_client.create_item(item_data)
        item_id = created_item_data.json().get("id")
        assert item_id is not None, f"ID не найден в ответе на создание: {created_item_data}"

        ValidateItemResponse.validate_response(created_item_data, ItemResponseModel, 200, item_data.model_dump())

        self.api_client.delete_item(item_id)
        print(f"Item с ID {item_id} успешно создан и удален.")
        return item_id

    def update_item_and_verify_changes(self, item_data):
        """
        Сценарий: обновить item и проверить, что данные изменились.
        """
        item_data_1 = item_data()
        item_data_2 = item_data()
        item_id = self.api_client.create_item(item_data_1).json().get("id")
        updated_item = self.api_client.update_item(item_id, item_data_2)

        ValidateItemResponse.validate_response(updated_item, ItemResponseModel, 200, item_data_2.model_dump())

        print(f"Item с ID {item_id} успешно обновлен.")
        self.api_client.delete_item(item_id)
        return item_id

    def delete_existing_item_and_verify(self, item_data):
        """
        Сценарий: удалить существующий booking и убедиться, что он удален.
        """
        item_data = item_data()
        item_id = self.api_client.create_item(item_data).json().get("id")

        self.api_client.delete_item(item_id)
        print(f"Item с ID {item_id} отправлен на удаление.")
        return item_id
