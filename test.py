import os, sys

dir_path="./pj_doc"
#image_fname = "centos:latest"
image_fname = "biocontainers/python-bz2file:v0.98-1-deb_cv1"
#command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.[0].Descriptor.digest'"
command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.Descriptor.digest'"
command="sudo docker manifest inspect "+ image_fname +" -v"
os.system(command)