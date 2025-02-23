import azure.functions as func
from .main import unified_handler  # Use a relative import

def main(req: func.HttpRequest) -> func.HttpResponse:
    return unified_handler(req)