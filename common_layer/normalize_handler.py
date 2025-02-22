# normalize_handler.py
import json

def normalize_handler(func):
    """
    A decorator that normalizes incoming request data for both AWS Lambda and Azure Functions.
    
    For AWS Lambda (API Gateway), it expects an event containing 'queryStringParameters'
    and a 'body' (as a JSON string). For Azure Functions, it uses req.params and req.get_json().
    
    The decorator merges both the query parameters and the body into a single dictionary
    and passes that dictionary to the decorated function.
    """
    def wrapper(*args, **kwargs):
        normalized_event = {}
        # AWS Lambda: event and context provided.
        if len(args) == 2:
            event, context = args
            # Extract query string parameters.
            query_params = event.get("queryStringParameters") or {}
            # Extract and parse the body if present.
            body = {}
            if event.get("body"):
                try:
                    body = json.loads(event["body"])
                except Exception:
                    body = {}
            # Merge body and query string parameters.
            normalized_event = {**body, **query_params}
            response = func(normalized_event)
            return {
                "statusCode": 200,
                "body": response
            }
        # Azure Functions: a single HttpRequest object is provided.
        elif len(args) == 1:
            req = args[0]
            query_params = req.params or {}
            body = {}
            try:
                body = req.get_json()
            except Exception:
                body = {}
            normalized_event = {**body, **query_params}
            response = func(normalized_event)
            # Import here to avoid dependency issues on non-Azure environments.
            import azure.functions as func_azure
            return func_azure.HttpResponse(response, status_code=200, mimetype="application/json")
        else:
            raise Exception("Invalid number of arguments for handler")
    return wrapper
