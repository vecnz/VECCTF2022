FROM ubuntu:20.04

RUN apt-get update && apt-get install python3 socat -y 

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf
COPY pow.py .
COPY flag.txt .
COPY main.py .
COPY js .
RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 1337
ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 main.py'"]
