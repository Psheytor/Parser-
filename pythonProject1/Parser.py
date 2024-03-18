from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://omgtu.ru/ecab/persons/?b=0'
    page = requests.get(url, verify=False)

    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('div', style="padding: 5px; font-size: 120%;")

    file = open('FIO.txt', 'w')
    for i in block:
        result=i.text
        file.write(result+"\n")


