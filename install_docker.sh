#!/bin/bash
# installing docker on Ubunut 14.04 LTS
# run this shell script as super user
apt-get install linux-image-extra-`uname -r` -y
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
apt-get update
apt-get install lxc-docker -y
# Try something like
# sudo docker run ubuntu /bin/bash
# To do away typing sudo before every docker command run the docker-no-sudo.sh file as the home user. 
