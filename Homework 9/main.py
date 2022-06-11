from bs4 import BeautifulSoup
import requests

class Currency:
    dollar_url = 'https://www.google.com/search?client=firefox-b-d&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.149 Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0
    difference = 3

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(',', '.'))
    def get_currency_price(self):
        full_page = requests.get(self.dollar_url, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.find_all('span', {
            'class': 'DFlfde SwHCTb', 'data-precision': '2'
            }
            )
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(',', '.'))
        print('Курс доллара на текущий момент = ' + str(currency))
        num1 = int(input("долларів: "))
        num2 = currency
        r = num1 + num2
        print(r)

currency = Currency()
currency.check_currency()