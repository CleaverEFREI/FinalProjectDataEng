pipeline{
    agent any
    
    stages{
        stage('NPM Build'){
            steps{
                bat "pytest"
                bat "docker-compose up -d"
            }
        }
    }
}