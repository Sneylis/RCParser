import requests
from bs4 import BeautifulSoup
import urllib3

def ParsRC (json_file):
    urllib3.disable_warnings()
    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    response = requests.get("https://bdu.fstec.ru/vul", headers, verify=False)

    soup = BeautifulSoup(response.content, 'html.parser')

    input_item = soup.find('input', {'placeholder': 'Введите слово или словосочетание'})


    print('sdsds',input_item)





ParsRC('output.json')

