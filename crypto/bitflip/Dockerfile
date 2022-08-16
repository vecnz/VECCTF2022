FROM ubuntu:18.04

RUN apt update  && apt install socat python3 python3-pip -y
RUN python3 -m pip install pycryptodome
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf


COPY main.py .
COPY flag.txt .
RUN chown -R root:root /home/ctf
USER ctf


CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/usr/bin/python3 main.py"