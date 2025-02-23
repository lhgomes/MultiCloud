# MultiCloud Deployment Project

This project demonstrates a unified codebase for deploying a Python-based function to both AWS Lambda and Azure Functions. The solution is structured to isolate business logic from cloud integration code.

The objective is to show how a **Cloud Agnostic** solution can utilize **Cloud Native** services from both **Azure** and **AWS**, while keeping implementation differences in the **CI/CD pipeline** instead of the application code.

## Overview

- Business Logic (business_logic.py): Contains the core functionality, such as processing records or calculations.
- Abstract Interfaces (interfaces.py): Defines interfaces that decouple business logic from cloud-specific implementations.
- AWS Implementations (azure_impl.py): Uses AWS services (e.g., DynamoDB, S3, Lambda).
- Azure Implementations (aws_impl.py): Uses Azure services (e.g., CosmosDB, Blob Storage, Functions).
- Unified Handler (normalize_handler.py): A common entry point that normalizes input and routes execution to the correct business logic.

### Key Features:
- Uses **Azure** services:  
  - Azure Function Apps  
  - CosmosDB  
- Uses **AWS** services:  
  - API Gateway  
  - AWS Lambda  
  - DynamoDB  
- Implements a **multi-cloud strategy** without tightly coupling the application to a single provider.
- Ensures **code portability**, with cloud-specific differences handled in the deployment pipeline.

## Architecture

The project follows a **cloud-agnostic approach**, where:
- Business logic remains **consistent** across different cloud providers.
- Cloud-specific implementations are managed via **infrastructure as code** (IaC) and CI/CD pipelines.

## Getting Started

### Prerequisites

To run this project, ensure you have the following installed:
- **Python** 
- **Azure CLI** and **AWS CLI** (for cloud interactions)
- **Git** for version control
  
## Deployment

### AWS Lambda

- Packaging: The Makefile creates a zip package that includes a top-level folder (e.g., package) so that AWS Lambda can import modules with absolute imports.
- Handler Configuration: Set the Lambda handler to package.main.lambda_handler.

### Azure Functions

- Packaging: The Makefile also creates a deployment package for Azure with a proper structure including host.json, requirements.txt, .python_packages, and the MyFunction folder.
- Handler: The function’s __init__.py in MyFunction uses relative imports to load unified_handler from main.py.

## GitHub Actions

The project uses GitHub Actions for automated deployment. The workflow includes:
- Building and packaging the code for both AWS and Azure.
- Deploying to AWS Lambda (using the AWS CLI).
- Deploying to Azure Functions (using the Azure/functions-action with scm-do-build-during-deployment: true).

## Configuration

- Environment Variables:
  - For AWS: Configure environment variables such as DYNAMODB_TABLE.
  - For Azure: Configure settings like COSMOSDB_ENDPOINT, COSMOSDB_KEY, AZURE_FUNCTION_APP_NAME, etc. Use a local.settings.json file for local development (do not deploy it).
- Secrets:
  Store sensitive information (e.g., AWS keys, Azure credentials) in GitHub Secrets.

## Running Locally

To test locally:
1. For Azure Functions, place local.settings.json in the project root (next to host.json) and run:
     func start
2. For AWS Lambda, simulate the package structure by running:
     python -m package.main

## License

MIT License
