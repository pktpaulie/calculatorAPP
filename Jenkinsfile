pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        echo 'Hello World'
        sh '''pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: \'SECONDS\')
    }
    stages {
        stage(\'Test\') {
            steps {
                echo \'Hello World\'
            }
        }
    stage(\'Deploy\') {
            steps {
                echo \'Hello World\'
            }
        }
    }
}'''
        }
      }

    }
    options {
      timeout(time: 1, unit: 'SECONDS')
    }
  }