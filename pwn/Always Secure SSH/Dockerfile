FROM alpine:latest

# install required packages
RUN apk add --no-cache openssh busybox-extras rsync

# generate ssh keys
RUN ssh-keygen -A
RUN ssh-keygen -N "" -f ~/.ssh/id_rsa

# Setup chroot
RUN adduser --disabled-password --gecos "" ctf
RUN mkdir chroot
RUN rsync -aqz --exclude /chroot / /chroot 2>/dev/null || :
RUN chmod -R 555 /chroot
RUN chmod 666 /chroot/dev/null

# move ssh keys
RUN cp /chroot/root/.ssh/id_rsa.pub /chroot/root/.ssh/authorized_keys
RUN echo 'command="cat /flag.txt"' $(cat ~/.ssh/id_rsa.pub) > ~/.ssh/authorized_keys

# make everything owned by root so read only
RUN chown root:root -R /chroot/home/ctf

# secure the root account password
RUN echo "root:$(($RANDOM))" | chpasswd

# setup flag and script
COPY flag.txt flag.txt
COPY script.sh script.sh
RUN chmod +x script.sh

# init docker
ENTRYPOINT []
CMD ["/bin/ash", "-c", "/usr/sbin/sshd -D & nc -lkp 9999 -e /script.sh"]
EXPOSE 9999