pipeline{
    agent any
    environment{
        VENV_DIR ='venv'
        GCP_PROJECT= "gen-lang-client-0866277301"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"

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
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
        stage("building and push to gcr"){
            steps{
               withCredentials([file(credentialsId:'gcp-key',variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                script{
                    echo 'building and pushing to gcr'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}
                    gcloud auth configure-docker --quiet 
                    docker build --tag gcr.io/${GCP_PROJECT}/mlops-test:latest .
                    docker push gcr.io/${GCP_PROJECT}/mlops-test:latest 
                    '''
                }
               }
            }
        }
    
    stage("deploy google run"){
            steps{
               withCredentials([file(credentialsId:'gcp-key',variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                script{
                    echo 'deploy google run'
                    sh '''
                    export PATH=$PATH:${GCLOUD_PATH}
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${GCP_PROJECT}
                    gcloud run deploy mlops-test \
                        --image=gcr.io/${GCP_PROJECT}/mlops-test:latest \
                        --platform=managed \
                        --region=us-central1 \
                        --allow-unauthenticated
                    '''
                }
               }
            }
        }
    }
    
}