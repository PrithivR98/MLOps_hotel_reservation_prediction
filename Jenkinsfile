pipeline {
    agent any

    environment {
        VENV_DIR = 'mlops_project1'
        GCP_PROJECT = 'crack-linker-459016-n5'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {
        stage('Cloning Github repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github_token',
                            url: 'https://github.com/PrithivR98/MLOps_hotel_reservation_prediction.git'
                        ]]
                    )
                }
            }
        }

        stage('Setting up virtual environment and installing dependencies') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building and pushing docker image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing docker image to GCR'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }

        stage('DEPLOY TO GOOGLE CLOUD RUN') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'DEPLOY TO GOOGLE CLOUD RUN'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud run deploy ml-project \
                            -- image = gcr.io/${GCP_PROJECT}/ml-project:latest \
                            -- platform=managed \
                            -- region = us-central1 \
                            -- allow = unauthenticated
                        '''
                    }
                }
            }
        }
    }
}
