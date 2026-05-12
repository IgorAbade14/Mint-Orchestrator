#!/bin/bash
set -e

# 1. Caminhos
SCRIPT_PATH=$(realpath "$0")
ROOT_DIR=$(dirname "$(dirname "$SCRIPT_PATH")")
cd "$ROOT_DIR"

IMAGE_NAME="mint-orchestrator"
VERSION=$(date +%H%M) 

echo "🚀 Iniciando Deploy da Versão: $VERSION"

# 2. Build local 
echo "🔨 Building Docker image localmente..."
docker build -t $IMAGE_NAME:$VERSION .

# 3. Carregar manualmente para o Minikube
echo "🚚 Carregando imagem no cluster..."
minikube image load $IMAGE_NAME:$VERSION

# 4. Atualizar o YAML (Garantindo que o ImagePullPolicy seja correto)
echo "☸️ Atualizando manifestos..."
sed -i "s|image: $IMAGE_NAME:.*|image: $IMAGE_NAME:$VERSION|g" k8s/deployment.yaml

# Força o Kubernetes a NUNCA buscar na internet, apenas usar a imagem carregada
if ! grep -q "imagePullPolicy" k8s/deployment.yaml; then
    sed -i "/image: $IMAGE_NAME:$VERSION/a \        imagePullPolicy: IfNotPresent" k8s/deployment.yaml
fi

kubectl apply -f k8s/deployment.yaml  
kubectl apply -f k8s/service.yaml 

echo "⏳ Aguardando os novos Pods..."
# Aguarda os pods ficarem prontos (timeout de 90 segundos) 
kubectl wait --for=condition=ready pod -l app=mint-orchestrator --timeout=90s

echo "✅ Deploy Finalizado! Versão $VERSION no ar."
minikube service mint-orchestrator-service --url