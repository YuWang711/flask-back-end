pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
      }
    }

    stage('error') {
      steps {
        script {
          step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.prod.yml', option: [$class: 'ExecuteCommandInsideContainer', command: 'docker-compose -f docker-compose.prod.yml up -d --build', index: 1, privilegedMode: false, service: 'flask-app', workDir: ''],
          useCustomDockerComposeFile: true])
        }

      }
    }

  }
}