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
                    sh "docker login -u kudddy -p Zs0996755 http://ourhost:5100"
                    echo 'build image'
                    def customImage = docker.build("kudddy/catcher")
                    echo 'push image'
                    customImage.push()
                }
            }
        }
    }
}