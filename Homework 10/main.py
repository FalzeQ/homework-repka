from bs4 import BeautifulSoup
import requests
from datetime import datetime
import sqlite3

now = datetime.now()
response = requests.get('https://www.meteoprog.ua/ru/weather/Kyiv/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all('div', {'class': 'today-temperature'})
    res = soup_list[-1]
    print(res.text)

connection = sqlite3.connect('itstep_DB.sl3', 5)
cur = connection.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS  first_table (now FSP, res INT);')

try:
    cur.execute("INSERT INTO first_table (now, res) VALUES (now,res);")
except BaseException as error:
    print(type(error).__name__+": "+str(error))

connection.commit()
cur.execute('SELECT * FROM first_table')
print(cur.fetchall())
connection.close()