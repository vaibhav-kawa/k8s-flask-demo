# 5-Minute Video Demo Script

**0:00–0:30 Intro**
"Hi, I'm Vaibhav Kawa. In this demo I containerize a simple Flask web app with Docker and deploy it on Kubernetes using Minikube."

**0:30–1:15 Code walkthrough** (show files in VS Code)
- `app.py`: home page prints the pod name; `/health` is used for health checks.
- `Dockerfile`: slim Python base, requirements copied first for layer caching, non-root user, gunicorn server.

**1:15–2:00 Docker**
- `docker build -t flask-demo:1.0 .` → `docker images flask-demo`
- `docker run -d -p 5000:5000 --name flask-test flask-demo:1.0` → open localhost:5000 → `docker ps`
- "The app runs the same way on any machine with Docker."

**2:00–3:15 Kubernetes deploy**
- Explain `deployment.yaml`: 3 replicas, resource requests/limits, readiness and liveness probes.
- Explain `service.yaml`: NodePort, selects pods by label `app=flask-demo`, port 80 → 5000.
- `minikube image load flask-demo:1.0`, `kubectl apply -f k8s/`
- `kubectl get deployments`, `kubectl get pods -o wide`, `kubectl get svc`

**3:15–4:30 Show it working**
- `minikube service flask-demo-service --url` → open URL, refresh a few times → pod name changes (load balancing).
- `kubectl logs -l app=flask-demo --tail=10`
- Self-healing: `kubectl delete pod <name>` then `kubectl get pods` → a new pod appears.
- Scaling: `kubectl scale deployment flask-demo --replicas=5` → `kubectl get pods`.

**4:30–5:00 Wrap-up**
"Docker packaged the app, the Deployment keeps the desired number of pods running, and the Service gives a stable, load-balanced endpoint. Code is on GitHub. Thank you."
