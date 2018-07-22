FROM centos:7

RUN yum install -y openssh-server && \
    yum clean all

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/^HostKey/#HostKey/g' /etc/ssh/sshd_config && \
    sed -ri 's/^#(HostKey \/etc\/ssh\/ssh_host_rsa_key)/\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^(HostKey \/etc\/ssh\/ssh_host_dsa_key)/#\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^(HostKey \/etc\/ssh\/ssh_host_ecdsa_key)/#\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^(HostKey \/etc\/ssh\/ssh_host_ed25519_key)/#\1/' /etc/ssh/sshd_config

RUN rm -f /etc/ssh/ssh_host_*_key && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P ''

RUN echo "root:root" | chpasswd  && \
    echo "root   ALL=(ALL)       ALL" >> /etc/sudoers

CMD ["/usr/sbin/sshd", "-D"]