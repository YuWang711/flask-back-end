pipeline {
  agent any
  stages {
    stage('Docker Down') {
      steps {
        sh 'docker-compose -f docker-compose.prod.yml down'
      }
    }

    stage('Update code base') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
        archiveArtifacts '*'
      }
    }

    stage('docker compose') {
      steps {
        sh 'docker-compose -f docker-compose.prod.yml up -d --build'
      }
    }

  }
}