# CPU and Memory Monitoring App

This is a simple CPU and Memory monitoring application designed to work with AWS Elastic Kubernetes Service (EKS). It allows you to keep track of your cluster's resource utilization efficiently.

## Features

- Real-time CPU and Memory usage monitoring.
- Integration with AWS EKS for seamless deployment.
- Easy-to-use dashboard for visualizing resource statistics.
- Customizable alerts for resource thresholds.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- An AWS account with EKS access.
- Kubernetes cluster provisioned on AWS EKS.
- `kubectl` CLI installed and configured.
- Docker installed for local development.

### 1. Deploy the application to your EKS cluster:
```shell
kubectl apply -f k8s/
```
### 2. Access the monitoring dashboard:
```shell
kubectl port-forward service/monitoring-app 8080:80
```
Open your web browser and navigate to http://localhost:8080 to view the dashboard.

## For Local Development

1. [Install python 3.4 or above](https://www.python.org/downloads/)
2. Then, run the code below
```shell
pip3 install -r requirements.txt
```
requirements are now intalled for the project.

3. Now, run

```shell
python3 app.py
```

Now you App is currently running on your local machine.
