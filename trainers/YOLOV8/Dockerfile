FROM nvidia/cuda:11.6.2-devel-ubuntu20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/New_York

RUN apt-get update
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


RUN apt-get install -y python3.8
RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN apt-get install -y python3-pip
#RUN apt-get install -y python-dev python-setuptools

RUN python --version 

RUN mkdir projects
WORKDIR /projects/

RUN mkdir /projects/datasets

RUN pip install ultralytics==8.0.20
RUN pip install roboflow

COPY ./CODEBRIM_baseline.py /projects/