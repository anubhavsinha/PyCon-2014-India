# sudo not required anymore to run docker.
gpasswd -a ${USER} docker
service docker restart
# Now logout and then login.
