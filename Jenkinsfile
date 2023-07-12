pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh '''#!groovy
pipeline {
    agent any
    stage(\\\'Preparation\\\') {
        deleteDir()
        checkout scm
        sh \\\'git submodule update --init --recursive\\\'
        sh "/https://github.com/pktpaulie/calculator_proj.git/"
        #def workspace = pwd()
        sh "cd /var/jenkins_home/deploy-app-vars.yml ${workspace}/ci/ansible/"
        sh "cd /var/jenkins_home/ansible-hosts ${workspace}/ci/ansible/hosts"
        sh \\\'\\\'\\\'if [ ! -d "venv" ]; then
            virtualenv venv
        fi\\\'\\\'\\\'
        sh ". venv/bin/activate"
        sh "pip install django"
        sh "pip install behave"
        sh "pip install -r requirements.txt"
        sh "python manage.py makemigrations"
        sh "python manage.py migrate"
    }

}'''
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