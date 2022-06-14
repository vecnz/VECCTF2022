FROM ubuntu

RUN apt update && apt install socat python3 -y

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd


WORKDIR /home/ctf

COPY hash.py .
COPY flag.txt .

USER ctf
EXPOSE 8080
ENTRYPOINT socat TCP-LISTEN:8080,fork,reuseaddr,bind=0.0.0.0 EXEC:"python3 hash.py"