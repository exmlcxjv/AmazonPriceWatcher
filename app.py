import requests
import time
from bs4 import BeautifulSoup

URL = "https://www.amazon.sg/JAPFREAK-Controller-Compatible-Nintendo-Switch/dp/B085MZ1TY6?ref_=Oct_DLandingS_PC_7c78162c_1&smid=A1N03V5GA3OVRF"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}



def check_price():
    page = requests.get(URL, headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_dealprice').get_text().strip()
    print(title)
    print(price)

while 1==1:
    check_price()
    time.sleep(5)