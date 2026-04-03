pipeline {
    agent any
    stages {
        stage('Setup Venv') {
            steps {
                sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export PYTHONPATH=$(pwd)
                    pytest
                 '''
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t aceest-fitness:1.1.2 .'
            }
        }
        stage('Docker Deploy') {
            steps {
                sh 'docker stop aceest-container || true && docker rm aceest-container || true'  
                sh 'docker run -d -p 5000:5000 --name aceest-container aceest-fitness:1.1.2'
            }
        }
    }
}
