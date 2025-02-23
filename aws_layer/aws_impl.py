# aws_impl.py
import boto3
import uuid
from interfaces import DataStore

class DynamoDBStore(DataStore):
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def save_values(self, value1: int, value2: int) -> None:
        self.table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'value1': value1,
                'value2': value2
            }
        )
