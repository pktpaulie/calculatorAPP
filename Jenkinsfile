pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh '''#!groovy

pipeline{
    agent any
    stages {
       stage(\'Setup Python Virtual ENV for dependencies\'){
       steps  {
            sh \'\'\'
            
            chmod +x ./envsetup.sh
            ./envsetup.sh
            \'\'\'}
        }
        stage(\'Setup Gunicorn Setup\'){
            steps {
                sh \'\'\'
                chmod +x ./gunicorn.sh
                ./gunicorn.sh
                \'\'\'
            }
        }
        stage(\'setup NGINX\'){
            steps {
                sh \'\'\'
                chmod +x ./nginx.sh
                ./nginx.sh
                \'\'\'
            }
        }
    }
}
'''
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