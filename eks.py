from kubernetes import config,client

config.load_kube_config()

api_client = client.ApiClient()

# Defined the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="monitering-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "monitering-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "monitering-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="monitering-app-container",
                        image="494939336703.dkr.ecr.us-east-1.amazonaws.com/monitering-app-cloud:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)


# Created the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)


# Defined the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="monitering-app-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "monitering-app"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Created the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)