# Minecraft Server on Kubernetes with Ngrok

This repository contains configurations for deploying a Minecraft server in a Kubernetes environment using Minikube and exposing it externally with Ngrok.

## Project Structure

```plaintext
minecraft-k8s/
├── compose.yaml                # original Docker compose file for the Minecraft server
├── kompose-result/             # auto-generated Kubernetes manifests from kompose
│   ├── minecraft-claim0-persistentvolumeclaim.yaml
│   ├── minecraft-deployment.yaml
│   ├── minecraft-service.yaml
├── manifests/                  # manually created Kubernetes manifests
│   ├── minecraft-configmap.yaml
│   ├── minecraft-deployment.yaml
│   ├── minecraft-namespace.yaml
│   ├── minecraft-pvc.yaml
│   ├── minecraft-service.yaml
```

### manifests/
Manually created Kubernetes manifests:
- `minecraft-configmap.yaml`: configuration for server properties
- `minecraft-deployment.yaml`: deployment of the Minecraft server Pod
- `minecraft-namespace.yaml`: namespace definition for isolation
- `minecraft-pvc.yaml`: Persistent Volume Claim for storing world data
- `minecraft-service.yaml`: LoadBalancer service for exposing the server

## Setup

1. Deploy the namespace:
   ```bash
   kubectl apply -f manifests/minecraft-namespace.yaml
   ```

2. Deploy the Persistent Volume Claim:
   ```bash
   kubectl apply -f manifests/minecraft-pvc.yaml
   ```

3. Apply the ConfigMap:
   ```bash
   kubectl apply -f manifests/minecraft-configmap.yaml
   ```

4. Deploy the Minecraft server:
   ```bash
   kubectl apply -f manifests/minecraft-deployment.yaml
   ```

5. Expose the service:
   ```bash
   kubectl apply -f manifests/minecraft-service.yaml
   ```

6. Use Ngrok to expose the server to the public:
   ```bash
   ngrok tcp 25565
   ```

## Challenges
- Addressed connectivity issues with Minikube's NodePort and LoadBalancer limitations.
- Configured Ngrok for external server access due to firewall restrictions.

## Credits
Inspired by Minikube and Kubernetes documentation and the Ngrok tunneling solution.
