# Stage 1: Build Stage

FROM python:3.8-slim as Build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*  # Cleanup to reduce image size

    COPY . .

    RUN pip install --no-cache-dir flask mysqlclient

    # Stage 2: Production Stage

    FROM python:3.8-slim

    WORKDIR /app

    COPY --from=Build /app /app

    EXPOSE 5000

    CMD ["python", "app.py"]