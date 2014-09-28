From ubuntu:14.04

#RUN apt-get install build-essentials
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install flask
RUN pip install elasticsearch
RUN mkdir /application
WORKDIR /application
CMD python search.py
