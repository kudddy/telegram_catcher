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
    stages {
        stage('Build image') {
            steps {
                echo 'Starting to build docker image'

                script {
                    echo 'logging in docker'
                    withCredentials([
                        usernamePassword(credentialsId: dockercreds, usernameVariable: 'USER', passwordVariable: 'PASS')
                    ]){

                    sh "docker login -u ${USER} -p ${PASS}"
                    }
                    echo 'OK'
                }
            }
        }
    }
}