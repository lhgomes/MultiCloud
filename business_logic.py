# business_logic.py
from common_layer.interfaces import DataStore

class Calculator:
    def __init__(self, datastore: DataStore):
        self.datastore = datastore

    def process_values(self, value1: int, value2: int) -> int:
        # Save the values to the datastore
        self.datastore.save_values(value1, value2)
        # Return the sum of the two values
        return value1 + value2