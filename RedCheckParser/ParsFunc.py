import time

import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib3
import json



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

    f_CVE = driver.find_element(By.XPATH,'//*[@id="search"]')

    with open('output.json', 'r') as file:
        data = json.load(file)


        bdu_data = {}

        for host,cves in data.items():
            bdu_data[str(host)] = []
            if cves:
                for cve in cves:
                    print(host)
                    f_CVE.clear()
                    f_CVE.send_keys(cve[4:])
                    time.sleep(5)
                    try:
                        err = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[1]/span')
                        print('None')
                    except:
                        bdu_data[host].extend(cve)

    with open('current_cve.json', 'w') as file:
        json.dump(bdu_data, file, indent=4)






