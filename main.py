import os, sys, subprocess, json
#import show_layers
#nano /etc/resolv.conf
#nameserver 8.8.8.8

'''
def search_dockerhub(image_name):
    command="sudo docker search "+ image_name
    os.system(command)

def get_hash(image_fname):
    #jq 설치 필요
    try:
        command="sudo docker manifest inspect "+ image_fname +" -v --insecure"
        output = subprocess.check_output(command, shell=True, encoding='utf-8')
    except:
        print('올바르지 않는 DOCKER IMAGE NAME 입니다.')
        sys.exit(0)

    #Ref로 갯수 확인
    c_ref = output.count('Ref')

    #1개 이상이면 OS 선택 가능하도록 구현
    if c_ref == 1:
        command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.Descriptor.digest'"
        hash_output = subprocess.check_output(command, shell=True, encoding='utf-8')
    else:
        #OS 출력
        command="sudo docker manifest inspect "+ image_fname +" -v | jq '.[].Descriptor.platform'"
        output = subprocess.check_output(command, shell=True, encoding='utf-8')
        print(output)
        #OS 선택
        num = int(input('What do you want docker image? '))
        command="sudo docker manifest inspect "+ image_fname +" -v | jq -r '.[%d].Descriptor.digest'"%num 
        hash_output = subprocess.check_output(command, shell=True, encoding='utf-8')
        print(hash_output)

    return hash_output
'''
def cve_total(image_fname):
    #trivy 설치 후 trivy 이미지를 가져온 후 실행
    #https://aquasecurity.github.io/trivy/v0.37/getting-started/installation/
    
    #CVE 총 개수 및 분류
    command_all="trivy image "+ image_fname
    # command = "trivy image -f json -o trivy_result_1.json "+ image_fname
    result_all = os.popen(command_all)
    result_total = result_all.readlines()
    total = result_total[3]
    output = total.replace("\n", "")
    return output

def cve_hc(image_fname):
    #HIGH, CRITICAL 내용
    #command_hc = "trivy image --severity HIGH,CRITICAL -f json -o trivy_results.json "+ image_fname
    command_hc = "trivy image --severity HIGH,CRITICAL -f json "+ image_fname
    data = os.popen(command_hc).read()
    return data
    

def to_json(data, cnum):
    list_c = []
    list_h = []

    data = json.loads(data)
    data = data["Results"]
    for x in data:
        for y in x['Vulnerabilities']:
            if y['Severity'] == 'HIGH':
                list_h.append(y['VulnerabilityID'])
            if y['Severity'] == 'CRITICAL':
                list_c.append(y['VulnerabilityID'])
    
    dic_hc = {'HIGH':list_h, 'CRITICAL':list_c}

    result = {'OUTPUT':cnum,'VulnerabilityID':dic_hc}

    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4)

'''
def show_image_layer(namespace, name, tag, digest):
    sh = show_layers.ShowHistory(20)
    print(sh.run(namespace, name, tag, digest))
'''
# 메인 함수
def main():
    #image_name=str(input("docker hub image: "))
    #search_dockerhub(image_name)
    image_fname= input("docker hub image full name(ex.name:tag): ")
    #hash_output = get_hash(image_fname)
    if '/' in image_fname:
        namespace, name = image_fname.split('/')
        name, tag = name.split(':')
    else:
        namespace = 'library'
        name, tag = image_fname.split(':')
    #print(namespace, name, tag, hash_output)
    
    cnum = cve_total(image_fname)
    data = cve_hc(image_fname)
    to_json(data, cnum)
    #show_image_layer(namespace, name, tag, hash_output)

if __name__ == '__main__':
    main()