#!groovy

node {
    stage(\'Preparation\') {
        deleteDir()
        checkout scm
        sh \'git submodule update --init --recursive\'
        sh "https://github.com/pktpaulie/calculator_proj.git"
        def workspace = pwd()
        sh "cp ./var/jenkins_home/deploy-app-vars.yml ${workspace}/ci/ansible/"
        sh "cp /var/jenkins_home/ansible-hosts ${workspace}/ci/ansible/hosts"
        sh \'\'\'if [ ! -d "venv" ]; then
            virtualenv venv
        fi\'\'\'
        sh ". venv/bin/activate"
        sh "pip install django"
        sh "pip install behave"
        sh "pip install -r requirements.txt"
        sh "python manage.py makemigrations"
        sh "python manage.py migrate"
    }

}