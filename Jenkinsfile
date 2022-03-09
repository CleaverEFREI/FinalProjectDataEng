pipeline {
    agent any
    stages {
        stage('Stop running Docker Image and rerun') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up --build -d'
            }
        }
        stage('Testing') {
            steps {
                bat 'pytest'
                bat 'docker-compose down'
            }
        }
        stage('Switching branch') {
            steps {
                bat 'git checkout -f release'
            }
        }
    }
}
