from bs4 import BeautifulSoup
import requests


def get_btc_stock():
    html = requests.get('https://www.infomoney.com.br/cotacoes/bitcoin-btc/').content
    soup = BeautifulSoup(html, 'html.parser')

    btc_stock = soup.find('div', class_="value").find('p').get_text()
    return btc_stock


if __name__ == '__main__':
    print('BRL = ' + '{:10,.2f}'.format(float(get_btc_stock())))
