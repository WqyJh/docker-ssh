FROM alpine:latest

RUN printf '#!/bin/sh\n\
\n\
# Clear existing host keys and generate new ones.\n\
if [ ! -f /root/.ssh/known_hosts ]; then\n\
rm -f /etc/ssh/ssh_host_*_key &&\n\
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -P "" &&\n\
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -P "" &&\n\
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -P "" &&\n\
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -P "" \n\
fi\n\
\n\
exec /usr/sbin/sshd -D\n' \
> /entry-point.sh && \
    chmod +x /entry-point.sh && \
    apk add --no-cache openssh-server wget && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/^HostKey/#HostKey/g' /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd  && \
    echo "root   ALL=(ALL)       ALL" >> /etc/sudoers && \
    mkdir -p /root/.ssh && \
    mkdir -p /var/run/sshd

EXPOSE 22

CMD ["/entry-point.sh"]