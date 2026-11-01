# Flask on Docker + Kubernetes

A minimal Flask web app containerized with Docker and deployed to Kubernetes (Minikube).

Author: Vaibhav Kawa (PRN 202301040040)

## Project structure
```
app.py               Flask app ( / page shows the pod name, /health for probes )
requirements.txt     Python dependencies
Dockerfile           Image definition (slim base, layer caching, non-root user, gunicorn)
.dockerignore        Keeps the image small
k8s/deployment.yaml  Deployment: 3 replicas, resource requests/limits, health probes
k8s/service.yaml     NodePort Service exposing the app on port 30080
```

## 1. Docker
```bash
docker build -t flask-demo:1.0 .
docker images flask-demo
docker run -d -p 5000:5000 --name flask-test flask-demo:1.0
# open http://localhost:5000
docker ps
docker logs flask-test
docker stop flask-test && docker rm flask-test
```

## 2. Kubernetes (Minikube)
```bash
minikube start --driver=docker
minikube image load flask-demo:1.0      # make the local image available to the cluster
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get deployments
kubectl get pods -o wide
kubectl get svc
minikube service flask-demo-service --url   # open the printed URL
kubectl logs -l app=flask-demo --tail=20
```

## 3. Useful demo commands
```bash
kubectl scale deployment flask-demo --replicas=5   # scaling
kubectl delete pod <pod-name>                      # self-healing: a new pod is created
kubectl describe deployment flask-demo
```

## Cleanup
```bash
kubectl delete -f k8s/
minikube stop
```

## Cloud-native concepts shown
- **Container**: app + dependencies packaged into one portable image.
- **Pod**: smallest deployable unit in Kubernetes, runs the container.
- **Deployment**: declares the desired state (3 replicas) and keeps it true (self-healing, scaling, rolling updates).
- **Service**: stable network endpoint that load-balances traffic across pods selected by label.
- **Probes**: readiness/liveness health checks on `/health`.
- **Resource requests/limits**: fair scheduling and protection against runaway containers.
