import os, sys

# 함수
def search_dockerhub(image_name):
    command="sudo docker search "+ image_name
    os.system(command)

def print_hash(image_fname):
    #jq 설치 필요
    command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.[0].Descriptor.digest'"
    os.system(command)

def cve_test(image_fname):
    #trivy 설치 후 trivy 이미지를 가져온 후 실행
    #https://aquasecurity.github.io/trivy/v0.37/getting-started/installation/
    command="sudo docker run aquasec/trivy image "+ image_fname
    os.system(command)
    
# 메인 함수
def main():
    dir_path="./pj_doc"
    image_name=str(input("docker hub image: "))
    search_dockerhub(image_name)   #해당 함수는 search 기능 빼도 이상없음
    print("================================================================")
    image_fname=str(input("docker hub image full name(image:tag) "))
    print_hash(image_fname)
    print("================================================================")
    cve_test(image_fname)

if __name__ == '__main__':
    main()