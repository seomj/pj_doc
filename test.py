import os, sys

dir_path="./pj_doc"
docker_i = "centos:latest"
command="sudo docker manifest inspect "+ docker_i +" -v | jq -r '.[0].Descriptor.digest'"
os.system(command)