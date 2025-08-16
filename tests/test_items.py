import allure

from src.api.item_api_client import ItemApiClient
from src.scenarios.item_scenarios import ItemScenarios


class TestItems:
    @allure.title("Получение списка items")
    def test_get_and_verify_items_exist(self, auth_session):
        """
        Сценарий: получить список items и проверить, что он не пуст.
        """
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.get_and_verify_items_exist()

    @allure.title("Cоздание items")
    def test_create_booking_check_and_delete(self, auth_session, item_data):
        """
        Сценарий: создать item и сразу же его удалить.
        Возвращает ID созданного и удаленного item.
        """
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.create_item_check_and_delete(item_data)

    @allure.title("Изменение items")
    def test_update_item_and_verify_changes(self, auth_session, item_data):
        """
        Сценарий: обновить item и проверить, что данные изменились.
        """
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.update_item_and_verify_changes(item_data)

    @allure.title("Удаление items")
    def test_delete_existing_item_and_verify(self, auth_session, item_data):
        """
        Сценарий: удалить существующий item и убедиться, что он удален.
        """
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.delete_existing_item_and_verify(item_data)
