# 🚀 Jenkins Pipeline Construction

A Python Flask web application with a complete Jenkins CI/CD pipeline featuring automated testing, Docker containerization, and multi-stage deployment. This project demonstrates advanced DevOps practices including continuous integration, continuous deployment, and pipeline automation.

---

# 📋 Internship Details

| Field              | Details                           |
| ------------------ | --------------------------------- |
| **Candidate Name** | Neeharika Shakthivelan            |
| **Intern ID**      | CITS4308                          |
| **Organization**   | CodTech IT Solutions Pvt. Ltd.    |
| **Domain**         | DevOps                            |
| **Project Title**  | Jenkins Pipeline Construction     |

---

# 📖 Project Overview

This project demonstrates how a Flask web application can be integrated into a fully automated Jenkins CI/CD pipeline. The pipeline automatically handles code checkout, dependency installation, test execution, Docker image building, and deployment — all triggered from a single GitHub push.

---

# 🎯 Objectives

- Build a multi-stage Jenkins CI/CD pipeline.
- Automate testing using pytest with coverage reports.
- Containerize the Flask application using Docker.
- Integrate GitHub with Jenkins for automated builds.
- Implement health checks and deployment verification.
- Follow DevOps best practices for pipeline construction.

---

# 🚀 Features

✅ Python Flask Web Application  
✅ Jenkins Multi-Stage Pipeline  
✅ Automated pytest Test Suite (7 tests)  
✅ Docker Containerization  
✅ Docker Compose Orchestration  
✅ GitHub Integration  
✅ Code Quality Checks (flake8)  
✅ Health Check Verification  
✅ Interactive API Dashboard UI  
✅ Production-ready Gunicorn Server  

---

# ⚙️ Jenkins Pipeline Stages

| Stage | Description |
| ----- | ----------- |
| 🔍 Checkout | Pulls latest code from GitHub |
| 🐍 Setup Python | Creates virtual environment and installs dependencies |
| 🧪 Run Tests | Executes 7 pytest tests with coverage report |
| 🔎 Code Quality | Runs flake8 linting checks |
| 🐳 Docker Build | Builds and tags Docker image |
| 🚀 Deploy | Stops old container and runs new one |
| ✅ Health Check | Verifies app is live at `/api/health` |

---

# 🏗️ System Architecture

```
GitHub Push
     │
     ▼
Jenkins Pipeline
     │
     ├── Checkout Code
     ├── Setup Python Env
     ├── Run Tests
     ├── Code Quality
     ├── Docker Build
     ├── Deploy Container
     └── Health Check
          │
          ▼
   Flask App (Port 5000)
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
| ---------- | ------- |
| Python 3.14 | Backend Development |
| Flask 3.0 | Web Framework |
| Jenkins | CI/CD Automation |
| Docker | Containerization |
| Docker Compose | Container Orchestration |
| pytest | Automated Testing |
| flake8 | Code Quality |
| Gunicorn | Production WSGI Server |
| GitHub | Source Control |

---

# 📁 Project Structure

```
jenkins-flask-pipeline/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── wsgi.py
└── README.md
```

---

# ⚙️ Installation and Setup

## Clone Repository

```
git clone https://github.com/neeha-04/jenkins-flask-pipeline.git
cd jenkins-flask-pipeline
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run Locally

```
python wsgi.py
```

## Run Tests

```
python -m pytest tests/ -v
```

## Run with Docker

```
docker build -t flask-pipeline-app .
docker run -p 5000:5000 flask-pipeline-app
```

---

# 🌐 API Endpoints

| Endpoint | Description |
| -------- | ----------- |
| `/` | Main Dashboard UI |
| `/api/health` | Health Check |
| `/api/info` | Application Information |
| `/api/greet/<name>` | Personalized Greeting |

---

# 🧪 Test Results

```
7 passed in 0.85s

✅ TestHealthEndpoint::test_health_returns_200
✅ TestHealthEndpoint::test_health_returns_json
✅ TestInfoEndpoint::test_info_returns_200
✅ TestInfoEndpoint::test_info_has_correct_fields
✅ TestGreetEndpoint::test_greet_valid_name
✅ TestGreetEndpoint::test_greet_invalid_name
✅ TestIndexPage::test_index_loads
```

---

# 🔧 Jenkins Setup

## Prerequisites

- Jenkins 2.555.3 LTS
- Java 21
- Docker Desktop
- Git

## Create Pipeline Job

1. Open Jenkins at `http://localhost:8080`
2. Click **New Item** → name it `flask-pipeline` → select **Pipeline**
3. Under Pipeline → select **Pipeline script from SCM**
4. SCM → **Git** → paste repo URL
5. Branch → `*/main`
6. Script Path → `Jenkinsfile`
7. Click **Save** → **Build Now**

---

# 📚 Learning Outcomes

Through this project, the following skills were developed:

- Jenkins Pipeline Configuration
- CI/CD Workflow Automation
- Docker Integration with Jenkins
- Automated Testing with pytest
- Code Quality Enforcement
- GitHub and Jenkins Integration
- Multi-stage Pipeline Design
- DevOps Best Practices
- Container Deployment
- Health Check Implementation

---

# ✅ Conclusion

The Jenkins Pipeline Construction project successfully demonstrates a complete CI/CD workflow for a Python Flask application. By integrating Jenkins with GitHub and Docker, the pipeline automates every step from code push to deployment, ensuring consistent and reliable software delivery.

This project provided hands-on experience with industry-standard DevOps tools and pipeline automation techniques.

---

# 🔗 Project Links

### GitHub Repository

https://github.com/neeha-04/jenkins-flask-pipeline

---

# 👩‍💻 Author

**Neeharika Shakthivelan**

DevOps Intern  
CodTech IT Solutions Pvt. Ltd.

**Intern ID:** CITS4308

---

## ⭐ Acknowledgement

This project was developed as part of the DevOps Internship Program offered by CodTech IT Solutions Pvt. Ltd. The internship provided practical exposure to Jenkins, CI/CD pipeline automation, Docker containerization, automated testing, and modern DevOps practices.
```
