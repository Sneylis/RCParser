import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib3
import json
from bs4 import BeautifulSoup



def ParsRC ():
    urllib3.disable_warnings()
    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    driver = webdriver.Firefox()
    driver.get('https://bdu.fstec.ru/vul')



    with open('output.json', 'r') as file:
        data = json.load(file)


        bdu_data = {}

        for host,cves in data.items():
            bdu_data[str(host)] = []
            if cves:

                for cve in cves:
                    f_CVE = driver.find_element(By.XPATH,'//*[@id="select2-chosen-17"]')
                    f_CVE.click()
                    s_CVE = driver.find_element(By.XPATH,'//*[@id="s2id_autogen17_search"]')
                    print(host)
                    s_CVE.clear()
                    s_CVE.send_keys(cve[4:])
                    time.sleep(6)
                    try:
                        s_CVE.send_keys(Keys.ENTER)
                        b_CVE = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/div/div[2]/form/div[11]/input[2]').click()
                        b_CVE = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[1]/table/tbody/tr/td[1]/h4/a')
                        if b_CVE:
                            bdu_data[host].extend(cve)
                    except:
                        print('None')

    with open('current_cve.json', 'w') as file:
        json.dump(bdu_data, file, indent=4)

ParsRC()




