# Docker SSH

This repository provides container images based on the official system distributions
with sshd service.
Think about that if you want to try a system and you don't want to install a virtual
machine, to run a docker container is a good choice.
However, when you run a base system image you'll find that it don't have a entry point
that can run background forever, it will just run and exit instantly.
To solve this problem, we can run a sshd service as its entry point
then we can connect to it by ssh.

## Usage

```bash
# Run container background
docker run -itd wqyjh/docker-ssh:ubuntu16.04

# Inspect the container IP
docker inspect <container name>

# Connect with ssh
# password is 'root'
ssh root@<container ip>
```
