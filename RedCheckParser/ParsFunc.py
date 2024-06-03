import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib3
import json

def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)


    for host, cves in data.items():
        for cve in cves:
            print (host, cve)


def ParsRC (json_file):
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


    f_CVE.send_keys('CVE-2024-2424')

    try:
        err = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[1]/span')
        print('None')
    except:
        pass




test = read_json('output.json')

print (test)

