// pipeline {
//   agent { docker { image 'python:3.7.2' } }
//   stages {
//     stage('build') {
//       steps {
//         sh 'pip install -r requirements.txt'
//       }
//     }
//     stage('test') {
//       steps {
//         sh 'python test.py'
//       }
//     }
//   }
// }

pipeline {
    agent any
    environment {
        DISABLE_AUTH = 'true'
        GOOGLE_PROJECT_ID = 'velvety-harbor-284611'
        GOOGLE_SERVICE_ACCOUNT_KEY = credentials('service_account_key');
        GOOGLE_APP_NAME = 'test'
    }
    stages {
        stage('Build image') {
            steps {
                echo 'Starting to build docker image'

                script {
                    echo 'logging in docker'
                    withCredentials([
                        usernamePassword(credentialsId: "dockerid", usernameVariable: 'USER', passwordVariable: 'PASS')
                    ]){

                    sh "docker login -u ${USER} -p ${PASS}"
                    }
                    echo 'OK'

                    def customImage = docker.build("gcr.io/${GOOGLE_PROJECT_ID}/${GOOGLE_APP_NAME}")

                    customImage.push()






                    echo 'log in gcloud'
                    sh """
                    /gcloud/google-cloud-sdk/bin/gcloud config set project ${GOOGLE_PROJECT_ID};
                    /gcloud/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file ${GOOGLE_SERVICE_ACCOUNT_KEY};
                    echo "After authentication gcloud";
                    /gcloud/google-cloud-sdk/bin/gcloud app deploy --image-url gcr.io/${PROJECT_ID}/${GOOGLE_APP_NAME}
                    """
                    echo 'log OK'

                }
            }
        }
    }
}