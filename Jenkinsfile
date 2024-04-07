pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'harishdocker557/DhaappPy'
        VERSION = "1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/yourgithubusername/your-repo.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${VERSION}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${VERSION}").push()
                    }
                }
            }
        }
        
        stage('Cleanup Local Images') {
            steps {
                script {
                    sh "docker rmi ${DOCKER_IMAGE}:${VERSION}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline execution successful.'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}
