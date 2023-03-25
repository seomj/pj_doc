import os, sys, subprocess
import show_layers

# 함수
def search_dockerhub(image_name):
    command="sudo docker search "+ image_name
    os.system(command)

def get_hash(image_fname):
    #jq 설치 필요
    #official image
    # command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.[0].Descriptor.digest'"
    #etc
    command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.Descriptor.digest'"
    hash_output = subprocess.check_output(command, shell=True, encoding='utf-8')
    return hash_output

def cve_test(image_fname):
    #trivy 설치 후 trivy 이미지를 가져온 후 실행
    #https://aquasecurity.github.io/trivy/v0.37/getting-started/installation/
    command="sudo docker run aquasec/trivy image "+ image_fname
    save_txt = input('Do you want to save CVE?(y/n) ')
    if save_txt=='y':
        txt_command = command + '> ./trivy_result.txt'
    os.system(txt_command)
    
def show_image_layer(namespace, name, tag, digest):
    sh = show_layers.ShowHistory(20)
    print(sh.run(namespace, name, tag, digest))

# 메인 함수
def main():
    dir_path="./pj_doc"
    image_name=str(input("docker hub image: "))
    search_dockerhub(image_name)   #해당 함수는 search 기능 빼도 이상없음
    print("================================================================")
    image_fname= input("docker hub image full name(ex.name:tag): ")
    hash_output = get_hash(image_fname)
    print(hash_output, end='')
    namespace, name = image_fname.split('/')
    name, tag = name.split(':')
    print("================================================================")
    cve_test(image_fname)
    show_image_layer(namespace, name, tag, hash_output)

if __name__ == '__main__':
    main()