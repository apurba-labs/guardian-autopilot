# 🛡 Guardian Autopilot

### AI-Powered Multi-Agent Incident Response Platform

**Built with Alibaba Cloud Qwen** • **An Open Source Project by Gotihub**

Guardian Autopilot is an AI-powered multi-agent incident response platform that detects exposed credentials, investigates security incidents, correlates historical investigations, evaluates operational risk, and generates executive incident reports using Alibaba Cloud Qwen.

Developers can interact with Guardian through a powerful CLI, REST API, or the Guardian Console, making it suitable for local development, cloud deployment, and production-ready security workflows.

---

# 🌐 Live Demo

### Guardian Console

https://guardian.gotihub.com

### API Documentation

https://guardian.gotihub.com/docs

---

# Architecture

![Architecture](docs/images/architecture.png)

---

# Guardian Console

![Guardian Console](docs/images/guardian-console.png)

---

# REST API

![Swagger](docs/images/swagger.png)

---

# Developer CLI

![CLI](docs/images/autopilot-cli.png)

---

# ✨ Features

- 🤖 AI Multi-Agent Incident Response
- 🔍 Intelligent Secret Detection
- 🧠 AI Security Investigation
- 🧠 Historical Incident Correlation
- 💾 Investigation Memory
- ⚖️ Human Approval Decision Engine
- 📄 Executive Incident Reports
- ⚡ FastAPI REST API
- 🖥 Interactive Streamlit Console
- 🐳 Docker Compose Deployment
- 🌐 Nginx Reverse Proxy
- ☁️ Alibaba Cloud ECS Deployment
- 🔒 HTTPS with Let's Encrypt

---

# 🏆 Why Guardian Autopilot?

Guardian Autopilot demonstrates a complete AI-powered incident response workflow.

Instead of treating every incident in isolation, Guardian remembers previous investigations and correlates repeated indicators to provide historical context for security analysts.

The platform can:

- Detect exposed credentials from text and logs
- Perform AI-assisted security investigations
- Correlate incidents with historical investigations
- Evaluate operational risk
- Determine human approval requirements
- Produce executive-ready incident reports
- Support CLI, REST API, and a web-based Guardian Console
- Run locally or on Alibaba Cloud ECS

---

# Project Architecture

```text
                     Internet
                         │
                         ▼
              guardian.gotihub.com
                         │
                HTTPS (Let's Encrypt)
                         │
                         ▼
               Docker Nginx Reverse Proxy
                  ┌──────────────┐
                  │              │
                  ▼              ▼
         Guardian Console     Guardian API
          Streamlit UI         FastAPI
                  │              │
                  └──────┬───────┘
                         ▼
               Guardian Orchestrator
                         │
      ┌────────┬──────────┬──────────┬────────┬────────┐
      ▼        ▼          ▼          ▼        ▼
    Parser  Investigation  Memory   Decision  Report
                            │
                            ▼
                 Historical Incident Store
                            │
                            ▼
                 Alibaba Cloud Qwen
```

---

# Quick Start

```bash
git clone https://github.com/apurba-labs/guardian-autopilot.git

cd guardian-autopilot

uv sync

cp .env.example .env
```

Configure

```env
DASHSCOPE_API_KEY=your_api_key
```

---

# CLI

```bash
guardian doctor

guardian explain fixtures/incidents/mixed_incident.txt

guardian serve
```

---

# REST API

```bash
guardian serve
```

Swagger

```
http://localhost:8000/docs
```

---

# Guardian Console

```bash
streamlit run src/ui/app.py
```

Open

```
http://localhost:8501
```

---

# Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

API

```
http://localhost:8000/docs
```

Console

```
http://localhost:8501
```

---

# 🧪 Verification & Testing

Run the following commands to verify Guardian Autopilot.

### Environment

```bash
guardian doctor
```

### Version

```bash
guardian version
```

### End-to-End Workflow

```bash
guardian explain fixtures/incidents/mixed_incident.txt
```

### Individual Agent Tests

Parser Agent

```bash
uv run python -m tests.integration.test_parser
```

Investigation Agent

```bash
uv run python -m tests.integration.test_investigation
```

Decision Agent

```bash
uv run python -m tests.integration.test_decision
```

Report Agent

```bash
uv run python -m tests.integration.test_report
```

Guardian Orchestrator

```bash
uv run python -m tests.integration.test_orchestrator
```

Alibaba Cloud Qwen Connectivity

```bash
uv run python -m tests.integration.test_alibaba_connection
```

---

### REST API

```bash
guardian serve
```

Swagger

```
http://localhost:8000/docs
```

---

### Guardian Console

```bash
streamlit run src/ui/app.py
```

Open

```
http://localhost:8501
```

---

# Production Deployment

Guardian Autopilot is deployed on **Alibaba Cloud ECS** using:

- Alibaba Cloud Qwen
- FastAPI
- Streamlit
- Docker Compose
- Dockerized Nginx Reverse Proxy
- HTTPS (Let's Encrypt)

---

# Technology Stack

- Python 3.12
- Alibaba Cloud ECS
- Alibaba Cloud Qwen
- FastAPI
- Streamlit
- Typer CLI
- Rich
- Docker
- Docker Compose
- Nginx
- uv

---

# Roadmap

## v1.0

- ✅ Multi-Agent Workflow
- ✅ Historical Incident Correlation
- ✅ Investigation Memory
- ✅ Guardian CLI
- ✅ REST API
- ✅ Guardian Console
- ✅ Alibaba Cloud Qwen
- ✅ Docker Deployment

## v1.1

- PDF Report Export
- React Dashboard
- GitHub Actions
- PyPI Package
- Docker Hub
- Kubernetes Deployment

---

# Contributing

Contributions are welcome.

Please open an Issue or Pull Request.

---

# License

MIT License

---

Built with ❤️ using Alibaba Cloud Qwen

An Open Source Project by **Gotihub**