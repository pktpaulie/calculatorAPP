pipeline {
  agent any
  stages {
    stage('Pre-build') {
      steps {
        sh '''#!groovy
pipeline{
    agent any
    stages {
    
        stage(\'Setup Python Virtual ENV for dependencies\'){
       
      steps  {
            sh \'\'\'
            chmod +x envsetup.sh
            ./envsetup.sh
            \'\'\'}
        }
        stage(\'Setup Gunicorn Setup\'){
            steps {
                sh \'\'\'
                chmod +x gunicorn.sh
                ./gunicorn.sh
                \'\'\'
            }
        }
        stage(\'setup NGINX\'){
            steps {
                sh \'\'\'
                chmod +x nginx.sh
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
      parallel {
        stage('Test') {
          steps {
            sh '''#!groovy

node {stage(\'Test\') 
{
        sh "python manage.py test"
     }
}'''
          }
        }

        stage('error') {
          steps {
            sh '''node {stage(\'Test\') 
{
   stage("BDD") {
        behave
    }
}'''
          }
        }

      }
    }

    stage('Staging-Deploy') {
      steps {
        sh '''node {    
     stage(\'Staging deploy\') {
        ansiColor(\'xterm\') {
            ansiblePlaybook(
                    colorized: true,
                    inventory: \'ci/ansible/hosts\',
                    playbook: \'ci/ansible/deploy-app-staging.yml\',
                    sudoUser: null
            )
        }
    }
}'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''stage(\'Production deploy approval\') {
    timeout(time: 5, unit: \'DAYS\') {
        def deploy = input(id: \'userInput\', message: \'Deploy to production?\')
    }
}

'''
        }
      }

      stage('Production') {
        steps {
          sh '''node {
    stage(\'Production deploy\') {
        ansiColor(\'xterm\') {
            ansiblePlaybook(
                    colorized: true,
                    inventory: \'ci/ansible/hosts\',
                    playbook: \'ci/ansible/deploy-app-production.yml\',
                    sudoUser: null
            )
        }
    }
}
'''
          }
        }

      }
    }