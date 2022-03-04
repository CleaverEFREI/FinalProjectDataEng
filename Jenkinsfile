pipeline{
    agent any
    
    stages{
        stage('NPM Build'){
            steps{
                bat "docker-compose -f docker-compose.yaml up -d"
            }
        }
    }
}