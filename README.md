# Azure ML Deployment Methods

This repo demonstrates different ML deployment methods on Azure.

Anyone needing to deploy using Azure can pick the most suitable deployment method and use the sample code here to by swapping in their model. Each notebook takes the model and deploys it to an endpoint hosted in Azure cloud for real-time inference. We show a range of methods using various Azure cloud model hosting and deployment tools.

A sample model ready for deployment is provided in the `models` folder. This model simulates a model in a production setting coming from:

- A continuous training stage in a CI/CD pipeline: see [notebook](models/sample_train_diabetes_model.ipynb) for sample training code.
- A registered model in a ML tracking registry such as MLFLow or Azure ML Workspace: see [notebook](models/sample_download_mlflow_model.ipynb) for sample download code.

## Get started

`sudo apt-get install --only-upgrade azure-cli`

`az login`

## Model tracking

Models can be tracked using Azure Machine Learning studio (**TODO** insert link) and can be registered or downloaded as appropriate at any time. Alternatively, you can use an external MLFlow (**TODO** insert link) model tracking workspace. However, at time of writing there is no support for deploying models from an external MLFlow to Azure. Note that, at time of writing, you can use `mlflow.deployments` via the `azureml-mlflow` plugin to wrap MLFlow syntax around [deploying an Azure Machine Learning workspace-tracked model to Azure Managed Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models?tabs=fromjob%2Cmir%2Ccli), which is the same method as (1). See [this article](https://www.mlflow.org/docs/latest/plugins.html#deployment-plugins) for latest MLFlow support.

## Model deployment

### 1. Deploy to Azure Managed Endpoints

See notebook [01 - Deploy AzureML endpoint](01%20-%20Deploy%20AzureML%20Endpoint/01%20-%20demo.ipynb)

This registers a ML model in the Azure Machine Learning workspace (**TODO** add link) and deploys it to [Azure Managed Endpoints](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints#managed-online-endpoints-vs-kubernetes-online-endpoints) using the [Azure Machine Learning Python SDK]()**TODO**: add link. Notes: 

- This uses the `azure-ai-ml` Python SDK v2 for interacting with Azure Machine Learning. This is the most up-to-date method and deprecates using `azureml-core`.
- Direct deployment from Azure Machine Learning to Azure Container Instances (ACI) is deprecated, see [this blog](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/transitioning-legacy-aci-inference-web-services-to-managed/ba-p/3628940) for info.


### 2. Deploy to Azure Function App - serverless approach

See notebook [03 - Deploy serverless endpoint](03%20-%20Deploy%20serverless%20endpoint/03%20-%20demo.ipynb)

This containerises a ML model and deploys to an Azure Function App, which is a lightweight serverless way of exposing a model to an inference endpoint.

### 3. Deploy to Azure Container Instances with custom container (BYOC)

See notebook [04 - Deploy with BYOC](04%20-%20Deploy%20with%20BYOC/04%20-%20demo.ipynb)

This gives the most flexibility without creating a dedicated compute instance. The model, inference script and API endpoint are all bundled into a Docker image, so that scoring, environment, load balancing can all be configured in the image. The image is pushed to Azure Container Registry (ACR) and deployed with Azure Container Instances (ACI).

### 4. Deploy to Azure App Service

[tutorial](https://joonasaijala.com/2021/05/31/how-to-easily-deploying-azure-machine-learning-models-to-azure-app-service/)

### 5. Deploy to Azure Kubernetes Service

[Azure Kubernetes endpoint](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-anywhere) with AKS ([sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/kubernetes/kubernetes-online-endpoints-simple-deployment.ipynb)), [more inspiration](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/ai/real-time-scoring-machine-learning-models?source=recommendations) 
