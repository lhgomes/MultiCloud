import azure.functions as func
from main import unified_handler  # Import your unified handler from main.py

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Simply forward the request to your unified handler.
    return unified_handler(req)