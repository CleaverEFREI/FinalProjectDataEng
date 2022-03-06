pipeline{
    agent any
    
    stages{        
        stage('Stop running Docker Image'){
            steps{
                bat 'docker-compose down'
            }
        }
        stage('Testing'){
            steps{
                bat "pytest"
            }
        }        
        stage('Switching to release branch'){
            steps{
                bat 'git checkout release'
            }
        }        
        stage('Deliver'){
            steps{
                bat 'git add .'
                bat 'git diff --quiet && git diff --staged --quiet || git commit -am "Change for release"'
                bat 'git push'
            }
    }
}