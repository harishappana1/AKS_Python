# for local testing in minikube
docker build -t newproject .
minikube start
eval $(minikube -p minikube docker-env)
kubectl apply -f deploymeny.yaml
kubectl appply -f service.yaml
kubectl get all
minikube service service_name # to access