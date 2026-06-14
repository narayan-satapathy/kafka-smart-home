# 🏠 Kafka Smart Home System

A real-time IoT simulation using Kafka and Python.

## Tech Stack
- Kafka
- Python
- Docker Compose

## Architecture
Sensors → Kafka → Consumer Services

## How to Run

### 1. Start Kafka
docker compose up -d

### 2. Create topic
./scripts/create_topics.sh

### 3. Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 4. Run consumers
python -m consumers.logger_service

### 5. Run producers
python -m producers.temperature_sensor

## Features
- Real-time streaming
- Multiple producers
- Multiple consumers
- Event-driven architecture
