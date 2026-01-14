
pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                echo 'Code is cloned automatically by Jenkins'
            }
        }

        stage('Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python app.py'
            }
        }
    }
}