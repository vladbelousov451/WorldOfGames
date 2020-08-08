node {
    def app

    stage('Clone repository') {
        /* Cloning the Repository to our Workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image */

        app = docker.build("vladibelousov54/worldofgame")
    }
    stage('reqired things'){
        sh "chmod 777 ./test/chromedriver"
	sh "wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm"
        sh "sudo yum install google-chrome-stable_current_x86_64.rpm -y"

    }

    stage('Test image') {
        echo "Testing Image"
        sh  "docker run -d -p 400:400 --name my_app vladibelousov54/worldofgame"
        dir('test'){
		echo "running python"
        	answer = sh 'python e2e.py'
		echo 'the answer is ${answer)'
		
        }
    }
    stage('Clean things'){
        sh "docker kill my_app"
        sh "yum remove google-chrome -y"
        sh "docker rm my_app"

    }
    stage('Push image') {
        /* 
			You would need to first register with DockerHub before you can push images to your account
		*/
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
            } 
                echo "Trying to Push Docker Build to DockerHub"
    }
    
}

