FROM centos:7


RUN echo -e '#!/bin/sh\n\
\n\
# Clear existing host keys and generate new ones.\n\
rm -f /etc/ssh/ssh_host_*_key &&\n\
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P "" &&\n\
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -P "" &&\n\
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -P "" &&\n\
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -P "" \n\
\n\
exec /usr/sbin/sshd -D\n' \
> /entry-point.sh && \
    chmod +x /entry-point.sh && \
    yum install -y openssh-server wget && \
    yum clean all && \
    wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && \
    chmod +x /usr/bin/dumb-init && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/^HostKey/#HostKey/g' /etc/ssh/sshd_config && \
    sed -ri 's/^#(HostKey \/etc\/ssh\/ssh_host_rsa_key)/\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^#(HostKey \/etc\/ssh\/ssh_host_dsa_key)/\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^#(HostKey \/etc\/ssh\/ssh_host_ecdsa_key)/\1/' /etc/ssh/sshd_config && \
    sed -ri 's/^#(HostKey \/etc\/ssh\/ssh_host_ed25519_key)/\1/' /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd  && \
    echo "root   ALL=(ALL)       ALL" >> /etc/sudoers && \
    mkdir -p /root/.ssh && \
    mkdir -p /var/run/sshd

EXPOSE 22

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

CMD ["/entry-point.sh"]