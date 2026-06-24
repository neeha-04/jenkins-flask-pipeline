Here's your README.md — paste this into the file:
markdown# 🚀 Jenkins Pipeline Construction — Advanced CI/CD Project

![Jenkins](https://img.shields.io/badge/Jenkins-2.555.3-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> **Codtech IT Solutions Internship — Task 4**  
> An advanced Jenkins CI/CD pipeline that automates building, testing, and deploying a Python Flask web application using Docker.

---

## 📌 Project Overview

This project demonstrates a complete CI/CD pipeline using Jenkins for a Python Flask application. The pipeline automatically handles everything from code checkout to deployment, including running tests and building Docker containers.

---

## 🏗️ Project Structure
jenkins-flask-pipeline/

├── app/

│   ├── init.py          # Flask app factory

│   ├── routes.py            # API routes

│   └── templates/

│       └── index.html       # Frontend UI

├── tests/

│   ├── init.py

│   └── test_app.py          # 7 automated tests

├── Dockerfile               # Container configuration

├── docker-compose.yml       # Multi-container setup

├── Jenkinsfile              # Pipeline definition

├── requirements.txt         # Python dependencies

├── wsgi.py                  # App entry point

└── README.md

---

## ⚙️ Jenkins Pipeline Stages

| Stage | Description |
|-------|-------------|
| 🔍 Checkout | Pulls latest code from GitHub |
| 🐍 Setup Python | Creates virtual environment, installs dependencies |
| 🧪 Run Tests | Executes 7 pytest tests with coverage report |
| 🔎 Code Quality | Runs flake8 linting checks |
| 🐳 Docker Build | Builds and tags Docker image |
| 🚀 Deploy | Stops old container, runs new one |
| ✅ Health Check | Verifies app is live at `/api/health` |

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Main dashboard UI |
| GET | `/api/health` | Returns app health status |
| GET | `/api/info` | Returns app & system info |
| GET | `/api/greet/<name>` | Returns personalized greeting |

---

## 🧪 Test Results
7 passed in 0.85s

✅ TestHealthEndpoint::test_health_returns_200

✅ TestHealthEndpoint::test_health_returns_json

✅ TestInfoEndpoint::test_info_returns_200

✅ TestInfoEndpoint::test_info_has_correct_fields

✅ TestGreetEndpoint::test_greet_valid_name

✅ TestGreetEndpoint::test_greet_invalid_name

✅ TestIndexPage::test_index_loads

---

## 🐳 Docker

```bash
# Build image
docker build -t flask-pipeline-app .

# Run container
docker run -d -p 5000:5000 flask-pipeline-app
```

---

## 🚀 Local Setup

```bash
# Clone the repo
git clone https://github.com/neeha-04/jenkins-flask-pipeline.git
cd jenkins-flask-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the app
python wsgi.py

# Run tests
python -m pytest tests/ -v
```

---

## 🔧 Jenkins Setup

1. Install Jenkins from [jenkins.io](https://jenkins.io)
2. Create a new **Pipeline** job
3. Set SCM to **Git** and paste repo URL
4. Set branch to `*/main`
5. Script path: `Jenkinsfile`
6. Click **Build Now**

---

## 👩‍💻 Author

**Neeharika Shakthivelan**  
DevOps Intern — Codtech IT Solutions  
[GitHub](https://github.com/neeha-04)
