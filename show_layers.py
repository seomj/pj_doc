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
            # divs = driver.find_elements(By.XPATH, "//div[@data-testid='imglayersLayerListItem']")
            divs = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[1]/div[2]/div")
            # //*[@id="mainContainer"]/div/div[3]/div
            # //*[@id="mainContainer"]/div/div[3]/div/div[1]/div[2]
            # //*[@id="mainContainer"]/div/div[3]/div/div[1]/div[2]/div
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
            driver.quit()
            return content
        except Exception as e:
            raise e

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--namespace', help = 'target namespace on Dockerhub', required = True)
#     parser.add_argument('--name', help = 'image name on github', required = True)
#     parser.add_argument('--tag', help = 'tag info of target image', required = True)
#     parser.add_argument('--digest', help = 'digest value of target image', required = True)
#     args = vars(parser.parse_args())
#     sh = ShowHistory(20)
#     print('Success!!:', sh.run(args['namespace'], args['name'], args['tag'], args['digest']))

# if __name__ == "__main__":
#     main()

#python3 main.py --namespace=bitnami --name centos-base-buildpack --tag=7-r9 --digest=sha256:312524d0394bd0d5eea04644d31a1084dcbe69ab4b6c42adc938a01ab94d15f8