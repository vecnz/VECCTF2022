FROM ubuntu:20.04

RUN apt update  && apt install python3 socat -y
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf
COPY pow.py .
COPY flag.txt .
RUN chown -R root:root /home/ctf
USER ctf

#Fav constant
EXPOSE 8537
CMD socat TCP-LISTEN:8537,reuseaddr,fork EXEC:"python3 pow.py"