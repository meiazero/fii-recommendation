import bs4 as bs
import requests
import re

'''
Scrapping to get the main infos from FIIs, like:
- name
- symbol
- admin

'''


def FilterCardsInfos(url, card_class):

    html = requests.get(url).text
    sp = bs.BeautifulSoup(html, 'html.parser')
    cards = sp.find_all('div', {'class': card_class})

    return cards


def FilterCardName(cards):
    names = []
    for card in cards:
        names.append(card.find('span', {'class': 'name'}))

    return RemoveTags(names)


def FilterCardSymbol(cards):
    symbols = []
    for card in cards:
        symbols.append(card.find('span', {'class': 'symbol'}))
    return RemoveTags(symbols)


def FilterCardAdmin(cards):
    admins = []
    for card in cards:
        admin = card.find('span', {'class': 'admin'})
        admins.append(admin)

    admins = RemoveTags(admins)
    return ClearAdminNames(admins)


def RemoveTags(list):
    cleared_data = []
    for item in list:
        cleared_data.append(re.sub(r'<[^>]*>', '', str(item)))
    return cleared_data


def ClearAdminNames(list):
    cleared_data = []
    for item in list:
        cleared_data.append(re.sub(r'[^a-zA-Z0-9]', '', str(item)))
    return cleared_data


'''

get the infos from the main page of the FII, requesting the url from the symbol, like:
- price
- DY
- Patrimonio Liquido
- Valor Patrimonial

'''


def GetMainPageInfosOfFII(symbol):
    pass


if __name__ == '__main__':
    GetMainPageInfosOfFII('KNRI11')
