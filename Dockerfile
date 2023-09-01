FROM ubuntu:22.04

WORKDIR /vpa

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 5000

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install --upgrade pip

COPY requirements.txt /vpa/
RUN pip3 install -r requirements.txt

COPY . /vpa/

RUN apt-get install -y libportaudio2
