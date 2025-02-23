# main.py
import os
import json
from .business_logic import Calculator
from .common_layer.normalize_handler import normalize_handler

def get_datastore(running_environment):
    """
    Dynamically import and return the appropriate DataStore implementation based on environment.
    """
    if running_environment == "aws":
        from .aws_layer.aws_impl import DynamoDBStore
        table_name = os.getenv("DYNAMODB_TABLE", "default_table")
        return DynamoDBStore(table_name=table_name)
    elif running_environment == "azure":
        from .azure_layer.azure_impl import CosmosDBStore
        return CosmosDBStore(
            endpoint=os.getenv("COSMOSDB_ENDPOINT", ""),
            key=os.getenv("COSMOSDB_KEY", ""),
            database_name=os.getenv("COSMOSDB_DATABASE", ""),
            container_name=os.getenv("COSMOSDB_CONTAINER", "")
        )
    else:
        raise ValueError(f"Unsupported environment: {running_environment}")

@normalize_handler
def unified_handler(normalized_event, running_environment):
    """
    A unified handler that expects a merged dictionary of parameters.
    
    In this example, it expects keys 'value1' and 'value2', saves them to the datastore,
    and returns their sum in JSON format.
    """
    try:
        value1 = int(normalized_event.get("value1"))
        value2 = int(normalized_event.get("value2"))
    except (TypeError, ValueError):
        return json.dumps({"error": "Invalid input. 'value1' and 'value2' must be numbers."})
    
    datastore = get_datastore(running_environment)
    calc = Calculator(datastore)
    result = calc.process_values(value1, value2)
    return json.dumps({"result": result})

# For local testing (simulate an AWS Lambda invocation)
if __name__ == "__main__":
    # Simulated AWS Lambda event structure.
    simulated_event = {
        "queryStringParameters": {},
        "body": json.dumps({"value1": 10, "value2": 10})
    }
    print(unified_handler(simulated_event, None))
