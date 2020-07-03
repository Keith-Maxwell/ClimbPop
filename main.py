import requests
from bs4 import BeautifulSoup
from typing import Tuple


def printProgressBar(gymName: str, percent: int, bonus_text: str, length: int = 100):
    filled = '█' * (percent * length // 100)
    empty = '-' * (length - len(filled))
    print(f'\n{gymName} : {percent} %\t|\t{bonus_text}')
    print(f'|{filled}{empty}|\n')


def getFillPercent(URL: str) -> Tuple[int, str]:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    tag = soup.find_all("progress")[0]
    percent = tag['value']
    jauge = soup.find_all('div', class_='jauge')[0]
    text = jauge.find_all('span')[-1].text
    return int(percent), text


URL_Montreuil = "https://montreuil.arkose.com/"
URL_Nation = "https://nation.arkose.com/"
# URL_Massy = "https://massy.arkose.com/"

p, t = getFillPercent(URL_Montreuil)
printProgressBar("Arkose Montreuil", p, t)
p, t = getFillPercent(URL_Nation)
printProgressBar("Arkose Nation", p, t)
# p, t = getFillPercent(URL_Massy)
# printProgressBar("Arkose Massy", p, t)
