pipeline{
    agent any 

    enviroment {
        VENV_DIR = 'mlops_project1'
    }
    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/PrithivR98/MLOps_hotel_reservation_prediction.git']])
                }
            }
        }

        stage('Setting up our virutal enviroment and installing dependancies'){
            steps{
                script{
                    echo 'Setting up our virutal enviroment and installing dependancies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''                
                    }
            }
        }
    }
}