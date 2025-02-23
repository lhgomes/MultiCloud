# MultiCloud

## Overview

This project demonstrates how a **Cloud Agnostic** solution can utilize **Cloud Native** services from both **Azure** and **AWS**, while keeping implementation differences in the **CI/CD pipeline** instead of the application code.

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
