import os, sys

dir_path="./pj_doc"
docker_i = "centos:latest"
command="sudo docker run aquasec/trivy image "+ docker_i
os.system(command)