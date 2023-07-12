pipeline {
  agent any
  stages {

    stage('Git') {
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
    stage('Setup') {
      steps {
        sh \'\'\'if [ ! -d "venv" ]; then
            virtualenv venv
        fi\'\'\'
        sh ". venv/bin/activate"
        sh "pip install django"
        sh "pip install behave"
        sh "pip install pytest"
        sh "pip install -r requirements.txt"
        sh "python manage.py makemigrations"
        sh "python manage.py migrate"
        }
      }

    stage('Test') {
      steps {
        echo 'Testing..'
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
