# ---------- Base Image ----------
FROM python:3.12-slim

# ---------- Environment ----------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---------- System deps ----------
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---------- Install Poetry ----------
ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==$POETRY_VERSION"

# Disable venv inside container
RUN poetry config virtualenvs.create false

# ---------- Workdir ----------
WORKDIR /app

# ---------- Copy dependency files first (for caching) ----------
COPY pyproject.toml poetry.lock ./

# ---------- Install dependencies ----------
RUN poetry install --no-root --no-interaction --no-ansi

# ---------- Copy project ----------
COPY . .

# ---------- Expose port ----------
EXPOSE 8000

# ---------- Run ----------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]