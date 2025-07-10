FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./

RUN pip install uv
RUN uv sync

COPY src/ /app/src

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:create_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
