pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
      }
    }

    stage('version') {
      steps {
        sh 'docker --version'
        sh 'docker -l'
        sh 'docker compose version'
        sh 'curl --version'
        sh 'jq --version'
      }
    }

  }
}