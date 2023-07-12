pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        echo 'Building..'
        sh '''#!groovy

    stage('Build') {
      steps {
        echo 'Testing..'
        sh '''#!groovy
pipeline {
    agent any
    stage(\\\'Preparation\\\') {
        deleteDir()
        checkout scm
   
    }
}'''
      }
    }

    stage('Test') {
      steps {
        echo 'Testing....'
        sh '''stage(\'Test\') {
        sh "python manage.py test"
    }'''
        }
      }

      stage('Deploy') {
        steps {
          echo 'Deploying....'
        }
      }

    }
  }
