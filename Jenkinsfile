pipeline {
    agent any
    environment {
        PROJECT_DIR = '/home/wojcikmichal86/stronka'  // katalog projektu na PythonAnywhere
        VENV = '/home/wojcikmichal86/.virtualenvs/stronka_env/bin/activate'  // ścieżka do venv
    }
    stages {
        stage('Pull latest code') {
            steps {
                sh "cd $PROJECT_DIR && git pull"
            }
        }
        stage('Install dependencies') {
            steps {
                sh "cd $PROJECT_DIR && source $VENV && pip install -r requirements.txt"
            }
        }
        stage('Migrate database') {
            steps {
                sh "cd $PROJECT_DIR && source $VENV && python manage.py migrate"
            }
        }
        stage('Collect static files') {
            steps {
                sh "cd $PROJECT_DIR && source $VENV && python manage.py collectstatic --noinput"
            }
        }
        stage('Restart server') {
            steps {
                sh "touch $PROJECT_DIR/reload.py"  // lub: echo '' > reload.py, jeśli tak działa na PA
            }
        }
    }
}