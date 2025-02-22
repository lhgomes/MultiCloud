# interfaces.py
import abc

class DataStore(abc.ABC):
    @abc.abstractmethod
    def save_values(self, value1: int, value2: int) -> None:
        """Saves the provided values into the datastore."""
        pass
