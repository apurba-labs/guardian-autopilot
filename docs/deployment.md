# Deployment

## Local Development

```bash
uv sync
guardian serve
streamlit run src/ui/app.py
```

## Docker

```bash
docker compose up --build
```

## Alibaba Cloud ECS

1. Create an ECS instance
2. Install Docker
3. Clone the repository
4. Configure `.env`
5. Run:

```bash
docker compose up -d
```

## Environment Variables

- DASHSCOPE_API_KEY
- QWEN_BASE_URL
- QWEN_MODEL
- API_URL