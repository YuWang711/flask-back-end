pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
        archiveArtifacts '*'
      }
    }

    stage('version') {
      steps {
        sh 'docker --version'
        sh 'docker compose version'
        sh 'curl --version'
      }
    }

    stage('prune docker data') {
      steps {
        sh 'docker compose -f docker-compose.prod.yml up -d --build'
      }
    }

  }
}