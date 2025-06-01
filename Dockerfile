FROM python:slim
ENV PYTHONDONTWRITEBYTECODE = 1 \
    PYTHONUNBUFFERED = 1 \
workdir /app
run apt-get update && apt-get install -y --no-install-recommends \
    lipgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

copy . .
run pip install --no-cache-dir -e .
run python pipeline/training_pipeline.py
expose 5000
cmd ["python","app.py"]