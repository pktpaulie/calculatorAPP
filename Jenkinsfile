<<<<<<< HEAD

=======
pipeline {
  agent any
  stages {
    stage('Pre-build') {
      steps {
        sh '''node {
    def mvnHome
    stage(\'Preparation\') { // for display purposes
        // Get some code from a GitHub repository
        git \'https://github.com/pktpaulie/calculator_proj.git\'
        // Get the Maven tool.
        // ** NOTE: This \'M3\' Maven tool must be configured
        // **       in the global configuration.
        mvnHome = tool \'M3\'
    }
    stage(\'Build\') {
        // Run the maven build
        withEnv(["MVN_HOME=$mvnHome"]) {
            if (isUnix()) {
                sh \'"$MVN_HOME/bin/mvn" -Dmaven.test.failure.ignore clean package\'
            } else {
                bat(/"%MVN_HOME%\\bin\\mvn" -Dmaven.test.failure.ignore clean package/)
            }
        }
    }
    stage(\'Results\') {
        junit \'**/target/surefire-reports/TEST-*.xml\'
        archiveArtifacts \'target/*.jar\'
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
>>>>>>> e460324ff041f0cf6f5b7d4ae2b0ba8c259a81d1
