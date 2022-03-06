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
            withPythonEnv('python3') {
                bat 'pip install pytest'
                bat 'pytest'
            }
        }
        stage('Switching branch') {
            steps {
                bat 'git checkout release'
            }
        }
        stage('Push release to git') {
            steps {
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push'
            }
        }
    }
}
