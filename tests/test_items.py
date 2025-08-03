from src.api.item_api_client import ItemApiClient
from src.scenarios.item_scenarios import ItemScenarios


class TestItems:
    def test_get_and_verify_items_exist(self, auth_session):
        item_api_client = ItemApiClient(auth_session)
        item_scenarios = ItemScenarios(item_api_client)
        item_scenarios.get_and_verify_items_exist()
