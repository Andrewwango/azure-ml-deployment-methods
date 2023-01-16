# Azure ML Deployment Methods (MLOps)

This repo will demonstrate different ML deployment methods on Azure.

Anyone needing to deploy using azure can pick the most suitable deployment method and use the sample code here to by swapping in their model.

For each of the methods, we demonstrate training a simple scikit-learn model, and deploy it to an endpoint hosted in Azure cloud for real-time inference. We show a range of methods using various Azure cloud model hosting and deployment tools. The methods covered are as follows:

1. [ML model tracked on Azure ML deployed in endpoint hosted in ACI (Azure Container Instance)](01%20-%20Deploy%20AzureML%20Endpoint/01%20-%20demo.ipynb)
2. [ML model tracked on MLFlow deployed in an Azure Managed Endpoint](02%20-%20Deploy%20MLFlow%20endpoint/02%20-%20demo.ipynb)
3. [ML model deployed to a serverless Azure Function App environment](03%20-%20Deploy%20serverless%20endpoint/03%20-%20demo.ipynb)
4. [ML model wrapped in custom container deployed to ACI - a "bring your own container" (BYOC) approoach](04%20-%20Deploy%20with%20BYOC/04%20-%20demo.ipynb)

Each folder contains a notebook stepping through model training, tracking, deployment, testing and management.

## TODO

1. Update all Azure ML-based methods to [AML SDK v2](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-migrate-from-v1)
2. Change focus of existing methods to:
    1. [Azure Managed Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-managed-online-endpoints?tabs=python) via Azure ML: This replaces legacy Azure ML deployment to ACI, see [here](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/transitioning-legacy-aci-inference-web-services-to-managed/ba-p/3628940) for info 
    2. Ignore [MLFlow](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models?tabs=fromjob%2Cmir%2Ccli) option (which can deploy to Managed Endpoints, legacy ACI and AKS) 
    3. Bring your own container (BYOC) on Azure ACI (+ACR) 
    4. Serverless on Function Apps 
3. Add new methods:
    1. [Azure Kubernetes endpoint](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-anywhere) with AKS ([sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/kubernetes/kubernetes-online-endpoints-simple-deployment.ipynb)), [more inspiration](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/ai/real-time-scoring-machine-learning-models?source=recommendations) 
    2. Serverless as Web App (i.e. on App Service) ([tutorial](https://joonasaijala.com/2021/05/31/how-to-easily-deploying-azure-machine-learning-models-to-azure-app-service/)) 
4. Include pros and cons for each method, cost and speed considerations
5. Ditch the tracking completely, and make a not about how MLFlow is not very useful in this situation.
6. Package each option as “drop-in” options, potentially with all the IaC needed
7. Add other models e.g. a sentiment analysis model or other text classifier

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
