pipeline
{
    agent any

    stages{

        stage('checkout'){

            steps{ 
                sh 'python --version'
                sh 'docker --version'
                echo "Build"
                echo "BUILD_NUMBER -$env.BUILD_NUMBER"
                echo "BUILD_ID - $env.BUILD_ID"
                echo "JOB_NAME - $env.JOB_NAME" 
            }

        }
    }
    stage('Test'){
      
      steps{
        sh 'pytest'
      }
          

    }
    stage('Build docker image'){

        script{
            dockerImage=docker.build("7797/dash-app-image:${env.BUILD_TAG}")
        }

    }
    stage('push docker Image to '){
        steps{
            scripts{
                docker.withRegistry('','7797')
                dockerImage.push();
                dockerImage.push('latest')
             
             }
        }
    }
    post{

		always{
			echo "I am awesome. I run always"

		}
		success{
			echo "I run when you are succesfull"
			
		}
		failure{
			echo "I run when you are fail I am failed"
			
		}
 } 
}