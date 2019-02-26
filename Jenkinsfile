pipeline {
  agent any
  stages {
    stage('1') {
      steps {
        sh 'ls'
      }
    }
    stage('2') {
      steps {
        sh 'pwd'
      }
    }
    stage('3') {
      steps {
        sleep 10
      }
    }
    stage('4') {
      steps {
        sh 'pwd'
      }
    }
  }
}