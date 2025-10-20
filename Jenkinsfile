pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Set up Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
            }
        }
        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && PYTHONPATH=$PYTHONPATH:$(pwd)/ci_demo python -m unittest discover -s ci_demo/tests -p "test_*.py"'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
