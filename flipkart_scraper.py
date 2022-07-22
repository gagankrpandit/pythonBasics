import time
import random
import pandas as pd
import re
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

url = 'https://docs.google.com/spreadsheets/d/18sClQNUTVaQUHiHrplLFKtyfDPJfNxARKD1Sro0DuiU/edit#gid=0'
url1 = url.replace('/edit#gid=', '/export?format=csv&gid=')
col_list = ['flipkart_url']
df_new = pd.read_csv(url1, usecols = col_list)

print('Run Start >>>\n')
for i in tqdm(range(len(df_new)), desc = 'progress...'):
    x = requests.get(df_new.loc[i, 'flipkart_url'])
    if x.status_code <= 200 or x.status_code <= 299:
        pass
    elif x.status_code <= 500 or x.status_code <= 599:
        print('\n\nServer error\n')
        exit()
    time.sleep(random.randint(1,10))

    html = x.text
    soup = BeautifulSoup(html, 'lxml')
    price = soup.find('div', re.compile(r'_30jeq3 _16Jk6d')).text
    title = soup.find('span', re.compile(r'B_NuCI')).text
    price = price.replace('₹', '')
    price = float(price.replace(',', ''))
    df_new.loc[i, 'title'] = title
    df_new.loc[i, 'price'] = price
    df_new.to_csv('flipkart_price_comparison.csv', index = False)

df_old = pd.read_csv('flipkart_price_comparison.csv')

for i in range(len(df_old)):
    if df_old.loc[i, 'price'] == df_new.loc[i, 'price']:
        print('price has not changed')
    elif df_old.loc[i, 'price'] < df_new.loc[i, 'price']:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has increased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('flipkart_price_update_comparison.csv', index = False)
    else:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has decreased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('flipkart_price_update_comparison.csv', index = False)

print('\nRun End >>>')
