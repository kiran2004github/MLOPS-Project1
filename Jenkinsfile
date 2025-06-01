pipeline{
    agent any
    stages{
        stage("cloning github repo to jenkins"){
            steps{
                script {
                    echo 'cloning github repo '
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/kiran2004github/MLOPS-Project1.git']])
                }
            }
        }
    }
