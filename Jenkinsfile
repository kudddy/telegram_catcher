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

                    echo 'log in gcloud'
                    sh "sudo -s;
                    gcloud auth activate-service-account --key-file ${GOOGLE_SERVICE_ACCOUNT_KEY};
                    echo "After authentication gcloud";
                    gcloud config list;
                    "
                    echo 'log OK'

                }
            }
        }
    }
}