FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN printf '#!/bin/sh\n\
\n\
# Clear existing host keys and generate new ones.\n\
rm -f /etc/ssh/ssh_host_*_key &&\n\
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P "" &&\n\
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -P "" &&\n\
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -P "" &&\n\
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -P "" \n\
\n\
printf "#!/bin/sh\n\nexec /usr/sbin/sshd -D\n" > /entry-point.sh\n\
exec /usr/sbin/sshd -D\n' \
> /entry-point.sh && \
    set -ex && \
    chmod +x /entry-point.sh && \
    apt-get update && \
    apt-get install -y sudo vim openssh-server openssh-client wget python3 python3-pip htop tmux libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir torch torchvision tensorflow-gpu scipy opencv-python sklearn jieba ipython jupyter && \
    rm -rf /var/lib/apt/lists/* && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/^HostKey/#HostKey/g' /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd  && \
    echo "root   ALL=(ALL)       ALL" >> /etc/sudoers && \
    mkdir -p /root/.ssh && \
    mkdir -p /var/run/sshd

EXPOSE 22

CMD ["/entry-point.sh"]
