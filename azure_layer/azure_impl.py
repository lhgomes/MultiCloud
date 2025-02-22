# azure_impl.py
import uuid
from azure.cosmos import CosmosClient
from common_layer.interfaces import DataStore

class CosmosDBStore(DataStore):
    def __init__(self, endpoint: str, key: str, database_name: str, container_name: str):
        self.client = CosmosClient(endpoint, key)
        self.database_name = database_name
        self.container_name = container_name
        self.database = self.client.get_database_client(database_name)
        self.container = self.database.get_container_client(container_name)

    def save_values(self, value1: int, value2: int) -> None:
        item = {
            "id": str(uuid.uuid4()),
            "value1": value1,
            "value2": value2
        }
        self.container.create_item(body=item)
