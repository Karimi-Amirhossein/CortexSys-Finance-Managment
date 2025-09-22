# Base Image
FROM python:3.11-slim

# Environment 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Workdir 
WORKDIR /app

# Dependencies 
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Project Files 
COPY . .