pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
      }
    }

    stage('') {
      steps {
        sh 'docker-compose -f docker-compose.prod.yml up -d --build'
      }
    }

  }
}