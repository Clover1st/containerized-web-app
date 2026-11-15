# Containerized Web App

A Dockerized web application deployed on AWS EC2, built as part of my cloud engineering journey.

## Stack
- Python (web server)
- Redis (visit counter)
- PostgreSQL (user database)
- Docker & Docker Compose

## Features
- Multi-container setup with Docker Compose
- Persistent data storage with Docker Volumes
- Redis for fast in-memory visit tracking
- PostgreSQL for structured user data
- Deployed on AWS EC2

## Services
| Service | Description |
|---------|-------------|
| web | Python HTTP server |
| redis | Visit counter |
| postgres | User database |

## How to run locally
```bash
docker compose up
```
Then visit http://localhost:8080

## Author
Okediran Emmanuel Oluwasegun
