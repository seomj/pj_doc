import os, sys, subprocess

dir_path="./pj_doc"
image_fname = "centos:latest"
#image_fname = "biocontainers/python-bz2file:v0.98-1-deb_cv1"

command="sudo docker manifest inspect "+ image_fname +" -v"
output = subprocess.check_output(command, shell=True, encoding='utf-8')
#print(output)

c_ref = output.count('Ref')

if c_ref == 1:
    command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.Descriptor.digest'"
else:
    command="sudo docker manifest inspect "+ image_fname +" -v | jq '.[].Descriptor.platform'"
    output = subprocess.check_output(command, shell=True, encoding='utf-8')
    print(output)
    num = int(input('What do you want docker image? '))
    command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.[%d].Descriptor.digest'"%num 
    output = subprocess.check_output(command, shell=True, encoding='utf-8')
    print(output)
