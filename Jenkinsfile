pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/YuWang711/flask-back-end.git', branch: 'main', poll: true)
        script {
          step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.prod.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: true])
        }

        sh '''docker logs -f
> logs.txt'''
      }
    }

  }
}