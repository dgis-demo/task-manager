FROM ubuntu:18.04

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

RUN apt-get install locales -y
RUN locale-gen en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

RUN apt install python3.6 -y
RUN apt install python3-pip -y

RUN apt-get install zlib1g-dev libjpeg-dev netcat -y

RUN python3 -m pip install pip==19.3.1

COPY . /opt/app
RUN pip install pipenv
RUN pipenv install --system
RUN chmod -Rf 7777 /opt/app

ENTRYPOINT ["/opt/app/entrypoint.sh"]