# 🌿 Mint-Orchestrator

![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?logo=kubernetes)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?logo=docker&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Automation-4EAA25?logo=gnubash&logoColor=white)
![Python](https://img.shields.io/badge/Python-Flask-3776AB?logo=python&logoColor=white)

O **Mint-Orchestrator** é um projeto focado na automação completa do ciclo de vida de uma aplicação containerizada em um ambiente local de Kubernetes utilizando **Minikube**.

O principal objetivo é demonstrar práticas modernas de:

- Infraestrutura como Código (IaC)
- Automação de Deploy
- Orquestração de Containers
- Monitoramento de Infraestrutura
- Pipelines resilientes em ambiente local

---

# 🚀 Funcionalidades Principais

## 🔨 Build Automatizado

Script Bash responsável por:

- Gerenciar o contexto Docker
- Automatizar o processo de build
- Publicar imagens localmente no cluster

---

## 🏷️ Versionamento Dinâmico

Implementação de tags baseadas em timestamp para evitar problemas de cache como:

```bash
ImagePullBackOff
```

Garantindo que o Kubernetes sempre utilize a versão mais recente da aplicação.

---

## ☸️ Orquestração Kubernetes

Configuração completa utilizando:

- Deployments com múltiplas réplicas
- Load Balancing via Service
- Estratégias de atualização de imagem
- Escalabilidade local

---

## 📊 Dashboard de Infraestrutura

Interface web desenvolvida em **Python + Flask** com:

- Visual Dark Mode
- Monitoramento de Pods
- Status do cluster
- Visualização simplificada da infraestrutura

---

## ❤️ Health Checks

Configuração de:

- Liveness Probes
- Readiness Probes

Para garantir estabilidade e resiliência da aplicação.

---

# 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Runtime | Python 3.9 (Flask) |
| Containerização | Docker |
| Orquestração | Kubernetes (Minikube) |
| Automação | Bash Scripting |
| Sistema Operacional | Linux Mint |

---

# 📦 Como Executar

Certifique-se de possuir os seguintes requisitos instalados:

- Docker
- Minikube
- Kubectl

---

## Clone o repositório

```bash
git clone https://github.com/seu-usuario/mint-orchestrator.git
```

---

## Acesse a pasta do projeto

```bash
cd mint-orchestrator
```

---

## Execute o deploy automatizado

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

---

# 🧠 Desafios & Aprendizados

Durante o desenvolvimento, um dos principais desafios encontrados foi o gerenciamento de cache de imagens no Kubernetes utilizando a tag:

```bash
:latest
```

Isso causava inconsistências durante o deploy, pois o cluster frequentemente reutilizava imagens antigas.

## ✅ Solução Implementada

Foi criado um sistema de versionamento dinâmico utilizando timestamps diretamente no script de deploy.

Com isso:

- Cada build gera uma nova tag única
- O cluster sempre baixa a versão mais recente
- Elimina necessidade de intervenção manual
- Evita problemas de cache em ambiente local

---

# 📫 Contato

**Igor**  
Aspiring DevOps Engineer

---

# 📚 Sumário

- 🌿 Mint-Orchestrator
- 🚀 Funcionalidades Principais
- 🛠️ Tecnologias Utilizadas
- 📦 Como Executar
- 🧠 Desafios & Aprendizados
- 📫 Contato