# Data Quality Engineering study program CI-CD basics for DQE module

## Branching strategy

Git flow branching strategy have been chosen for a project.
According to **project info** in task description we have a scheduled release cycles. Also the type of the project is of Enterprise level. *Git flow* provides a clear branching strategy which enhances core review process as each feature branch is isolated from other code changes. *Git flow* provides solid workflow for a project bi-weekly pre-release and monthly release. Even though *git flow* provides slow feedback it has separate *hotfix* branch to address any incidents happening on production.


### Configure WSL ip address resolution.

It is possible that Jenkins server will not be accessible by **localhost:port** address in a browser or Jenkins server will not be able to resolve **github.com**. WSL resolution of ip address can be the reason for that. To configure that:
- Before starting Jenkins-container navigate to search and enter 'wsl'.
- Right-click and run as administrator.
- Login.
- Execute a command (you will need root privileges for that):
sudo nano /etc/resolv.conf
- Edit opened file by adding nameserver 8.8.8.8 (the first line after comments).
- Press **Ctrl+x** and then confirm the changes by pressing **Y** and **RETURN**. Only after those changes you should start the container.


### Running a container

To run a container execute the following command:

```docker run --name new_container -p 0.0.0.0:1433:1433 -p 8080:8080 -v jenkins_data:/var/jenkins_home jenkins:test```

### Configure HTTP tunnel for github-webhooks:

After starting a container open another CLI and enter commands to install and use ngrok tunnel to allow access to Jenkins server through web endpoint https://phoenix-proper-steadily.ngrok-free.app:

- ```docker exec -it new_container bash```
- ```curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list && apt update && apt install ngrok```
- ```ngrok config add-authtoken 2elwGnqXSHbU1ZVUeaXz0gTQlTN_34LZLxYQNS7ZM7MfWz3XN```
- ```exit```
- ```docker exec -it new_container ngrok http --domain=phoenix-proper-steadily.ngrok-free.app 8080```

### Final notes

GitHub repo should be configured with correct Payload URL (*https://phoenix-proper-steadily.ngrok-free.app/ghprbhook/*) and **Pull request** webhook event.

PAT (Personal Access Token) has been configured to access and manage repository. It is saved within container's attached volume at **/var/jenkins_home/pat.txt**
