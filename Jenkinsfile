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
        stage('Push release to git') {
            steps {
                bat 'git config --global user.email "louis.gailhac@efrei.net"'
                bat 'git config --global user.name "CleaverEFREI"'
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "JENKINS-$BUILD_ID"'
                bat 'git push'
            }
        }
    }
}
