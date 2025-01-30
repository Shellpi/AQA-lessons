pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
        TESTS_DIR = 'Tests'
    }

    parameters {
        string(name: 'Caption', defaultValue: '=== TESTING ===', description: '')
        booleanParam(name: 'JUNIT', defaultValue: true, description: '')
    }

    stages {
        stage('Shellpi_git') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/homework31']],
                    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'git_dir']],
                    userRemoteConfigs: [[credentialsId: 'git-creds', url: 'git@github.com:Shellpi/AQA-lessons.git']]
                ])
            }
        }

        stage('test-execution') {
            steps {
                script {
                    dir('git_dir/lesson_31/Tests'){
                        withPythonEnv('python3') {
                            sh """
                                echo "${Caption}"
                                pip install -r requirements.txt
                                # pytest has exit code 1 if tests fail. We return true to be able continue flow.
                                if [ -z "${JUNIT}" ]; then
                                    pytest -sv ./test_homework27.py --alluredir=${WORKSPACE}/allure-results
                                else
                                    pytest -sv ./test_homework27.py --alluredir=${WORKSPACE}/allure-results --junit-xml=test_output.xml
                                fi
                            """
                        }
                    }
                }
            }
            post {
                always {
                        allure includeProperties:
                        false,
                        jdk: '',
                        results: [[path: 'allure-results']]
                }
            }
        }
    }
}