# Containerized Web App

A Dockerized web application with user authentication, deployed on AWS EC2.
Built as part of my cloud engineering journey.

## Stack
- Python + Flask (web server)
- PostgreSQL (user database)
- Redis (visit counter)
- Docker & Docker Compose
- AWS EC2 (deployment)

## Features
- User registration and login
- Password hashing with SHA-256
- Visit counter with Redis
- Persistent data storage with Docker Volumes
- Auto-restart on failure
- PostgreSQL health checks before app startup

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home page with visit count |
| POST | /register | Register a new user |
| POST | /login | Login with existing account |
| GET | /users | List all registered users |

## How to run locally
```bash
docker compose up
```
Then visit http://localhost:8080

## How to register a user
```bash
curl -X POST http://localhost:8080/register \
  -H "Content-Type: application/json" \
  -d '{"username": "yourname", "password": "yourpassword"}'
```

## How to login
```bash
curl -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username": "yourname", "password": "yourpassword"}'
```

## Author
Okediran Emmanuel Oluwasegun
