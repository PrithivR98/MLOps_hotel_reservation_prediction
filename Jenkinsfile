pipeline{
    agent any 

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/PrithivR98/MLOps_hotel_reservation_prediction.git']])
                }
            }
        }
    }
}