FROM python:3.11-slim

WORKDIR /app

RUN pip install fastapi uvicorn

COPY mcp_server.py .

EXPOSE 8000

CMD ["uvicorn", "mcp_server:app", "--host", "0.0.0.0", "--port", "8000"]
