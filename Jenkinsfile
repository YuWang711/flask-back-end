pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
      }
    }

    stage('Deploy') {
      steps {
        script {
          step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.prod.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
        }

      }
    }

  }
}