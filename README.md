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


## Supported Containers

- ubuntu16.04
- ubuntu14.04
- debian9
- debian8
- centos7
- centos6
- alpine

nvidia/cuda:
- cuda10.0-runtime-ubuntu18.04
- cuda10.0-cudnn7-runtime-ubuntu18.04
- cuda10.0-devel-ubuntu18.04
- cuda10.0-cudnn7-devel-ubuntu18.04
- cuda9.2-runtime-ubuntu18.04
- cuda9.2-cudnn7-runtime-ubuntu18.04
- cuda10.0-runtime-ubuntu16.04
- cuda10.0-cudnn7-runtime-ubuntu16.04
- cuda10.0-devel-ubuntu16.04
- cuda10.0-cudnn7-devel-ubuntu16.04
- cuda9.2-runtime-ubuntu16.04
- cuda9.2-cudnn7-runtime-ubuntu16.04


## Contributing

### Requirements

Python: >= 3

```bash
pip install -r requirements.txt
```

### config.yml

```yaml
apt:
  ubuntu:
    - latest
    - 16.04
    - 14.04

yum:
  centos:
    - latest
    - 7
    - 6

alpine:
  alpine:
    - latest
```

The above `config.yml` is in corresponding to the following directory structure.

```bash
├── alpine
│   └── latest
│       └── Dockerfile
├── centos
│   ├── 6
│   │   └── Dockerfile
│   ├── 7
│   │   └── Dockerfile
│   └── latest
│       └── Dockerfile
└── ubuntu
    ├── 14.04
    │   └── Dockerfile
    ├── 16.04
    │   └── Dockerfile
    └── latest
        └── Dockerfile
```

### Generate Dockerfiles

After you modify the templates or the config.yml, you can run `generate.py` to apply these changes, 
which will generate new files or override the old ones.

```bash
python generate.py
```