pipeline {
  agent any
  stages {
    stage('Pre-build') {
      steps {
        sh '''#!groovy

node {
    stage(\\\'Preparation\\\') {
        deleteDir()
        checkout scm
        sh \\\'git submodule update --init --recursive\\\'
        sh "https://github.com/pktpaulie/calculator_proj.git"
        def workspace = pwd()
        sh "cp /var/jenkins_home/deploy-app-vars.yml ${workspace}/ci/ansible/"
        sh "cp /var/jenkins_home/ansible-hosts ${workspace}/ci/ansible/hosts"
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