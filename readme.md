# for local testing in minikube
docker build -t newproject .
minikube start
eval $(minikube -p minikube docker-env)
kubectl apply -f deploymeny.yaml
kubectl appply -f service.yaml
kubectl get all
minikube service service_name # to access
az ad sp create-for-rbac --name "github" --role Contributor --scopes /subscriptions/cce3c17d-78f8-4ca8-bd35-958f2279a09b --sdk-auth