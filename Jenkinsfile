pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/rushmash91/path_visualizer', branch: 'master')
      }
    }

    stage('') {
      steps {
        sh 'docker build -t python .'
      }
    }

  }
}