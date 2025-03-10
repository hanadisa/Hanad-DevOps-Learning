FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*  # Cleanup to reduce image size

RUN pip install --no-cache-dir flask mysqlclient

EXPOSE 5000

CMD ["python", "app.py"]

