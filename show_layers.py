import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

class ShowHistory:
    
    def __init__(self, wait):
        self.__base_url = 'https://hub.docker.com/layers'
        self.__timewait = wait

    def run(self, namespace, name, tag, digest):
        target_url = "%s/%s/%s/%s/images/%s?context=explore" %(self.__base_url, namespace, name, tag, digest.replace(':','-'))
        content = []
        #print(target_url)
        try:
            options = Options()
            options.add_argument('-headless')
            driver = Firefox(executable_path='geckodriver', options=options)
            driver.implicitly_wait(self.__timewait)
            driver.get(target_url)
            if namespace != 'library':
                #not official image
                #layer 선택
                divs = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div")
                # print("divs: ", divs)
                # print("divs length: ", len(divs))  #5개가 나와야 함(O)
                if divs:
                    for div in divs:
                        #click every layer info
                        driver.execute_script("arguments[0].click();", div)
                        #get details info on the right detail panel
                        driver.implicitly_wait(self.__timewait)
                        detail_div = driver.find_elements(By.XPATH, "//div[@data-testid='imglayersLayerInstruction']")
                        #detail_div = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[2]/div/div")
                        # print("detail_div:", detail_div)
                        # print(detail_div[0].text)
                        content.append(detail_div[0].text)
                        # print('===========================================')
            else:
                #officail image
                #/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div
                divs = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/div/div/div")
                # print("divs: ", divs)
                # print("divs length: ", len(divs))  #3개가 나와야 함
                if divs:
                    for div in divs:
                        #click every layer info
                        driver.execute_script("arguments[0].click();", div)
                        #get details info on the right detail panel
                        driver.implicitly_wait(self.__timewait)
                        #command 버튼
                        #/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div/button[3]
                        c_button = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div/button[3]")
                        c_button[0].click()
                        #get details info on the right detail panel
                        driver.implicitly_wait(self.__timewait)
                        detail_div = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/pre")
                        #/html/body/div[1]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/pre
                        print(detail_div[0].text)
                        # content.append(detail_div[0].text)
                        # print('===========================================')
            driver.quit()
            return content
        except Exception as e:
            raise e

#python3 main.py --namespace=bitnami --name centos-base-buildpack --tag=7-r9 --digest=sha256:312524d0394bd0d5eea04644d31a1084dcbe69ab4b6c42adc938a01ab94d15f8