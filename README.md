# Pre-Delinquency Data Engine (WIP)

## 📌 Architecture Overview
This repository contains the foundational infrastructure for a real-time, event-driven data pipeline designed to predict banking pre-delinquency. 

The architecture moves away from batch processing to a streaming-first approach, utilizing containerized microservices and a centralized feature store to serve ML models with low-latency data.

**Core Tech Stack:**
* **Infrastructure:** Docker, `docker-compose`
* **Feature Store:** Feast (Offline Parquet storage & Online SQLite registry)
* **Data Flow:** Python ETL, Transaction Streaming

## 🚀 Current Status (Phase 1: Complete)
The core plumbing and data storage mechanisms are currently implemented and tracking:
- [x] **Data Ingestion & ETL:** Automated scripts to simulate and load banking transaction histories.
- [x] **Feature Store Registry:** `feature_repo` fully initialized defining the strict schemas for model training.
- [x] **Streaming Infrastructure:** `stream_transactions` scaffolded to handle real-time event throughput.
- [x] **Containerization:** `docker-compose.yml` drafted for isolated microservice orchestration.

## 🗺️ Roadmap (Phase 2: Upcoming)
- [ ] Connect Kafka topics to the transaction streaming script.
- [ ] Implement the ML Inference Node (FastAPI/Flask wrapper) to pull from the Feast online store.
- [ ] Add strict JSON schema validation for incoming payload data.

---
*Note: This is an active work-in-progress focused on robust data engineering and orchestration.*
