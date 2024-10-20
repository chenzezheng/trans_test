pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:flask' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py' 
            }
        }
    }
}