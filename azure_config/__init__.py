import sys
import os

# Add the prepackaged dependencies folder to sys.path.
# Adjust the path as needed based on your package structure.
package_path = os.path.join(os.path.dirname(__file__), '..', '.python_packages')
if package_path not in sys.path:
    sys.path.append(package_path)

import azure.functions as func
from .main import unified_handler  # Use a relative import

def main(req: func.HttpRequest) -> func.HttpResponse:
    return unified_handler(req)