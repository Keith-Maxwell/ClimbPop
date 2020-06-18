import requests
from bs4 import BeautifulSoup


def printProgressBar(gymName: str, percent: int, length: int = 100):
    filled = '█' * (percent * length // 100)
    empty = '-' * (length - len(filled))
    print(f'{gymName} : {percent} %')
    print(f'|{filled}{empty}|\n')


def getFillPercent(URL: str) -> int:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    tag = soup.find_all(attrs={"class": "jauge"})[0].p
    percent = tag['data-value']
    return int(percent)


URL_Montreuil = "https://montreuil.arkose.com/"
URL_Nation = "https://nation.arkose.com/"
URL_Massy = "https://massy.arkose.com/"

printProgressBar("Arkose Montreuil", getFillPercent(URL_Montreuil))
printProgressBar("Arkose Nation", getFillPercent(URL_Nation))
printProgressBar("Arkose Massy", getFillPercent(URL_Massy))
