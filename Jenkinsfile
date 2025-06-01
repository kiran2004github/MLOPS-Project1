pipeline{
    agent any
    environment{
        VENV_DIR ='venv'
    }
    stages{
        stage("cloning github repo to jenkins"){
            steps{
                script {
                    echo 'cloning github repo '
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/kiran2004github/MLOPS-Project1.git']])
                }
            }
        }
        stage("cetting up venv and install req "){
            steps{
                script {
                    echo 'setting up'
                    sh '''
                    python -m venv $(VENV_DIR)
                    . $(VENV_DIR)/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
    
}