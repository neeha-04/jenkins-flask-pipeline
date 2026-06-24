pipeline {
    agent any

    environment {
        APP_NAME        = 'jenkins-flask-pipeline'
        DOCKER_IMAGE    = "flask-pipeline-app"
        DOCKER_TAG      = "${BUILD_NUMBER}"
        CONTAINER_NAME  = 'flask-app-container'
        APP_PORT        = '5000'
        VENV_DIR        = 'venv'
        PYTHON          = 'C:\\Users\\neeha\\AppData\\Local\\Python\\bin\\python.exe'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timeout(time: 20, unit: 'MINUTES')
        timestamps()
    }

    stages {

        stage('🔍 Checkout') {
            steps {
                echo '========== Checking out source code =========='
                checkout scm
                echo "Branch: ${env.GIT_BRANCH}"
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage('🐍 Setup Python Environment') {
            steps {
                echo '========== Setting up virtual environment =========='
                bat """
                    "%PYTHON%" -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    "%VENV_DIR%\\Scripts\\pip.exe" install --upgrade pip
                    "%VENV_DIR%\\Scripts\\pip.exe" install -r requirements.txt
                """
            }
        }

        stage('🧪 Run Tests') {
            steps {
                echo '========== Running Test Suite =========='
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    "%VENV_DIR%\\Scripts\\pytest.exe" tests/ -v --cov=app --cov-report=term-missing
                """
            }
            post {
                failure {
                    echo '❌ Tests FAILED! Pipeline stopping.'
                }
                success {
                    echo '✅ All tests PASSED!'
                }
            }
        }

        stage('🔎 Code Quality Check') {
            steps {
                echo '========== Checking code style =========='
                bat """
                    "%VENV_DIR%\\Scripts\\pip.exe" install flake8
                    "%VENV_DIR%\\Scripts\\flake8.exe" app/ --max-line-length=100 --ignore=E501,W503,E302,W293,W292 || echo "Warnings found but continuing..."
                """
            }
        }

        stage('🐳 Docker Build') {
            steps {
                echo '========== Building Docker Image =========='
                bat """
                    docker build -t %DOCKER_IMAGE%:%DOCKER_TAG% .
                    docker tag %DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_IMAGE%:latest
                    echo Docker image built successfully!
                """
            }
        }

        stage('🚀 Deploy Container') {
            steps {
                echo '========== Deploying Application =========='
                bat """
                    docker stop %CONTAINER_NAME% 2>nul || echo "No container to stop"
                    docker rm %CONTAINER_NAME% 2>nul || echo "No container to remove"
                    docker run -d ^
                        --name %CONTAINER_NAME% ^
                        -p %APP_PORT%:5000 ^
                        --restart unless-stopped ^
                        %DOCKER_IMAGE%:latest
                    echo Container deployed!
                """
            }
        }

        stage('✅ Health Check') {
            steps {
                echo '========== Verifying Deployment =========='
                bat """
                    timeout /t 5 /nobreak
                    curl -f http://localhost:%APP_PORT%/api/health || exit 1
                    echo Application is healthy!
                """
            }
        }
    }

    post {
        success {
            echo """
            ╔══════════════════════════════════════╗
            ║   ✅ PIPELINE SUCCEEDED!              ║
            ║   App running on port ${APP_PORT}          ║
            ║   Build #${BUILD_NUMBER}                   ║
            ╚══════════════════════════════════════╝
            """
        }
        failure {
            echo """
            ╔══════════════════════════════════════╗
            ║   ❌ PIPELINE FAILED!                 ║
            ║   Check logs above for details       ║
            ╚══════════════════════════════════════╝
            """
        }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}