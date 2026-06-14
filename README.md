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

Project architecture--

kafka-smart-home/
│
├── common/
│   └── event_schema.py
│
├── producers/
│   ├── temperature_sensor.py
│   ├── motion_sensor.py
│   └── door_sensor.py
│
├── consumers/
│   ├── security_service.py
│   ├── climate_service.py
│   └── logger_service.py
│
├── scripts/
│   └── create_topics.sh
│
├── docker-compose.yml
├── requirements.txt
└── README.md



---------------

List of Events sent to kafka

        ┌────────────────────┐
        │  IoT Sensors       │
        │────────────────────│
        │ Temperature Sensor │
        │ Motion Sensor      │
        │ Door Sensor        │
        └─────────┬──────────┘
                  │
                  ▼
        Kafka Topic: smart-home-events
                  │
   ┌──────────────┼──────────────┐
   ▼              ▼              ▼
Security      Climate       Logger
Service       Service       Service
