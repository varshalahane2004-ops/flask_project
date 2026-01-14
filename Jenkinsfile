pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                echo "Code is cloned automatically by Jenkins SCM"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python script.py'
            }
        }
    }
}