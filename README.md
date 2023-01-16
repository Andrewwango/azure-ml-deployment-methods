# Azure ML Deployment Methods (MLOps)

This repo will demonstrate different ML deployment methods on Azure.

Anyone needing to deploy using azure can pick the most suitable deployment method and use the sample code here to by swapping in their model.

For each of the methods, we demonstrate training a simple scikit-learn model, and deploy it to an endpoint hosted in Azure cloud for real-time inference. We show a range of methods using various Azure cloud model hosting and deployment tools. The methods covered are as follows:

1. [ML model tracked on Azure ML deployed in endpoint hosted in ACI (Azure Container Instance)](01%20-%20Deploy%20AzureML%20Endpoint/01%20-%20demo.ipynb)
2. [ML model tracked on MLFlow deployed in an Azure Managed Endpoint](02%20-%20Deploy%20MLFlow%20endpoint/02%20-%20demo.ipynb)
3. [ML model deployed to a serverless Azure Function App environment](03%20-%20Deploy%20serverless%20endpoint/03%20-%20demo.ipynb)
4. [ML model wrapped in custom container deployed to ACI - a "bring your own container" (BYOC) approoach](04%20-%20Deploy%20with%20BYOC/04%20-%20demo.ipynb)

Each folder contains a notebook stepping through model training, tracking, deployment, testing and management.

## 1. Azure ML model deployment

See notebook [01 - Deploy AzureML endpoint](01%20-%20Deploy%20AzureML%20Endpoint/01%20-%20demo.ipynb)

This tracks a ML model in the Azure ML workspace and deploys it using the Azure ML core Python library. The model is deployed to an ACI instance using an automatically created inference script.

## 2. MLFlow model deployment

See notebook [02 - Deploy MLFlow endpoint](02%20-%20Deploy%20MLFlow%20endpoint/02%20-%20demo.ipynb)

## 3. Serverless deployment

See notebook [03 - Deploy serverless endpoint](03%20-%20Deploy%20serverless%20endpoint/03%20-%20demo.ipynb)

## 4. BYOC approach

See notebook [04 - Deploy with BYOC](04%20-%20Deploy%20with%20BYOC/04%20-%20demo.ipynb)

This gives the most flexibility without creating a dedicated compute instance. The model, inference script and API endpoint are all bundled into a Docker image, so that scoring, environment, load balancing can all be configured in the image. The image is pushed to Azure Container Registry (ACR) and deployed with Azure Container Instances (ACI).