FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu16.04

RUN apt-get update && \
    apt-get install -y openssh-server && \
    rm -rf /var/lib/apt/lists/*

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/^HostKey/#HostKey/g' /etc/ssh/sshd_config

RUN rm -f /etc/ssh/ssh_host_*_key && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P '' && \
    ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -P '' && \
    ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -P '' && \
    ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -P ''

RUN echo "root:root" | chpasswd  && \
    echo "root   ALL=(ALL)       ALL" >> /etc/sudoers

RUN mkdir -p /root/.ssh && \
    mkdir -p /var/run/sshd

CMD ["/usr/sbin/sshd", "-D"]