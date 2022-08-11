FROM ubuntu:18.04

RUN apt update  && apt install socat -y
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf


COPY not_simple_bof .
COPY flag.txt .
RUN chown -R root:root /home/ctf
USER ctf


CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"./not_simple_bof"