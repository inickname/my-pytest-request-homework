from src.api.item_api_client import ItemApiClient
from src.scenarios.item_scenarios import ItemScenarios


class TestItems:
    def test_get_and_verify_items_exist(self, auth_session):
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.get_and_verify_items_exist()

    def test_create_booking_check_and_delete(self, auth_session, item_data):
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.create_item_check_and_delete(item_data)

    def test_update_item_and_verify_changes(self, auth_session, item_data):
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.update_item_and_verify_changes(item_data)

    def test_delete_existing_item_and_verify(self, auth_session, item_data):
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.delete_existing_item_and_verify(item_data)
