FROM ubuntu:18.04

RUN apt update  && apt install python3 socat gcc -y
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf
COPY arr.py .
COPY flag.txt .
RUN chown -R root:root /home/ctf
USER ctf
CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 arr.py"
