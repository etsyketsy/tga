FROM continuumio/miniconda:4.4.10

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && apt-get upgrade -y && apt-get install -qqy \
    wget \
    bzip2 \
    libssl-dev \
    openssh-server

RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i '/PermitRootLogin/c\PermitRootLogin yes' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir -p /app | \
    mkdir -p /media-files | \
    mkdir -p /static-files

COPY ./app/requirements.yml /app/requirements.yml
RUN /opt/conda/bin/conda env create -f /app/requirements.yml

ENV PATH /opt/conda/envs/app/bin:$PATH
RUN sed '$ a conda activate app' -i /root/.bashrc


COPY ./app /app

COPY ./scripts/* /scripts/
RUN chmod +x /scripts/*

WORKDIR /app

EXPOSE 8000
EXPOSE 22
