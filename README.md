# Projeto – Plataforma de Microserviços Containerizada com Docker, Kubernetes e CI/CD

## 📌 Visão Geral
Este projeto tem como objetivo demonstrar a construção de uma arquitetura **containerizada**, utilizando **Docker Compose para ambiente local** e **Kubernetes para um cenário mínimo de produção**, contemplando boas práticas de **CI/CD, segurança, observabilidade, deploy e escalabilidade**.

O foco é apresentar uma solução funcional, organizada e alinhada com padrões utilizados em ambientes profissionais.

---

## 🧱 Arquitetura
A aplicação segue uma arquitetura **multi-serviço**, onde cada componente roda em seu próprio contêiner.

**Principais características:**
- Serviços isolados e independentes
- Comunicação via rede interna
- Variáveis de ambiente centralizadas
- Pronta para execução local e deploy em cluster Kubernetes

---

## 🐳 Ambiente Local com Docker Compose

### Pré-requisitos
- Docker
- Docker Compose

### Subindo o ambiente
Com um único comando, todos os serviços são inicializados:

```bash
docker compose up -d
```

### O que é configurado

- Arquitetura multi-serviço funcional

- Redes internas para comunicação entre serviços

- Volumes para persistência de dados

- Variáveis de ambiente definidas via .env ou diretamente no docker-compose.yml

```bash
docker compose down
```

---

## 📦 Conteinerização e Versionamento

### Dockerfiles

- Estruturados seguindo boas práticas

- Uso de multi-stage build quando aplicável

- Redução de camadas e dependências desnecessárias

- Execução com usuário não-root para maior segurança

### Versionamento de imagens
As imagens seguem versionamento semântico:

```bash
nome-da-imagem:1.0.0
```

---

## ☸️ Kubernetes – Produção Mínima
Os manifests estão organizados na pasta k8s/

### Aplicando os manifests
```bash
kubectl apply -f k8s/
```

### Health Checks

- Readiness Probe: garante que o pod só receba tráfego quando estiver pronto

- Liveness Probe: permite reinício automático em caso de falha

### Segurança

- Considerações baseadas em Pod Security Admission (baseline/restricted)

- Justificativa documentada no relatório técnico, considerando o escopo acadêmico e ambiente controlado

---

### 🔁 CI/CD

O projeto conta com um pipeline automatizado que executa:

### Etapas do pipeline

- Build da aplicação

- Execução de testes

- Build das imagens Docker

- Publicação das imagens em registry

- Validações básicas (lint e testes)

### Segurança no pipeline

- Secrets gerenciados via variáveis seguras da plataforma de CI

- Nenhuma credencial sensível versionada no repositório

## 📊 Observabilidade, Deploy e Escala

### Observabilidade

- Logs: saída padrão dos contêineres (stdout/stderr)

- Métricas: proposta conceitual baseada em CPU, memória e latência

- Traces: estratégia conceitual de tracing distribuído para rastreamento de requisições entre serviços

### Estratégia de Deploy

- Rolling Update

- Zero downtime

- Simplicidade operacional

- Suporte nativo do Kubernetes

### Escalabilidade

- Estratégia baseada em HPA (Horizontal Pod Autoscaler) de forma conceitual

- Escalonamento alinhado ao consumo de CPU/memória

- Justificada mesmo sem Metrics Server instalado, conforme escopo do projeto

---

## 📂 Estrutura de Pastas (resumo)

.
├── docker-compose.yml
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── secret.yaml
├── ci/
│   └── pipeline.yml
└── README.md

---

## 📄 Observações Finais

Este projeto foi desenvolvido com foco em boas práticas de engenharia, organização e clareza, priorizando entendimento conceitual e aplicação prática dos principais pilares de DevOps e Cloud Native.