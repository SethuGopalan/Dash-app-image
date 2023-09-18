pipeline {
    agent any
    
    environment {
        // Define environment variables as needed
        DOCKER_REGISTRY = '7797'
        DOCKER_IMAGE_NAME = 'dash-app-image'
        DOCKER_IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your GitHub repository
                checkout scm
            }
        }
        stage('Install and Run') {
            steps {
                // Create a virtual environment
                sh 'python -m venv venv'

                // Activate the virtual environment
                sh 'source venv/bin/activate'

                // Install packages using pip in the virtual environment
                sh 'pip install pytest'

                // Run your Python script or tests
                sh 'pytest'
            }
        }
        // stage('Test'){
        //     steps{
        //         sh '!pip install pytest'
        //         sh 'pytest'
        //     }
        // }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Authenticate with your Docker registry (if needed)
                    // You may need to provide credentials to your Docker registry here

                    // Push the Docker image to the registry
                    sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}"
                }
            }
        }
    }
    
    post {
        

        always{
            echo "I am awesome. I run always"

        }
        success{
            echo "I run when you are succesfull"
            
        }
        failure{
            echo "I run when you are fail I am failed"
            
        }
    }
 
}