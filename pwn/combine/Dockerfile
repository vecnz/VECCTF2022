FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive" TZ="Pacific/Auckland"
RUN apt-get update && apt-get install python3 python3-pip git curl socat -y 

WORKDIR /spidermonkey_build

RUN git clone https://github.com/glandium/git-cinnabar git-cinnabar --depth 1
ENV PATH="${PATH}:/spidermonkey_build/git-cinnabar"
RUN /spidermonkey_build/git-cinnabar/download.py
RUN pip3 install Mercurial

RUN curl https://hg.mozilla.org/mozilla-central/raw-file/default/python/mozboot/bin/bootstrap.py -O
RUN python3 bootstrap.py --vcs git --no-interactive --application-choice "SpiderMonkey JavaScript engine"

WORKDIR /spidermonkey_build/moz_config
COPY normal_config .
ENV MOZCONFIG="/spidermonkey_build/moz_config/normal_config"
WORKDIR /spidermonkey_build/mozilla-unified

#This is the most recent, but just in case they update it
RUN git checkout 41a24211b15a0717ff4bd407575f409cd5842390

COPY arr.patch .
RUN git apply arr.patch
RUN ./mach build

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
WORKDIR /home/ctf
COPY pow.py .
COPY flag.txt .
RUN chown -R root:root /home/ctf
USER ctf

COPY pow.py .
COPY main.py .
EXPOSE 1337

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 main.py'"]
