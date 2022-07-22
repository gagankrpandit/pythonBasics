import time
import random
import pandas as pd
import re
from re import sub
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from decimal import Decimal

url = 'https://docs.google.com/spreadsheets/d/1iyW8P_UFaqw4rODmOzmfsSJX5xfnx4x2eCl-mmQj_GY/edit#gid=0'
url1 = url.replace('/edit#gid=', '/export?format=csv&gid=')
col_list = ['amazon_url']
df_new = pd.read_csv(url1, usecols = col_list)

print('Run Start >>>\n')
for i in tqdm(range(len(df_new)), desc = 'progress...'):
    x = requests.get(df_new.loc[i, 'amazon_url'])
    if x.status_code <= 200 or x.status_code <= 299:
        print('\n\nSuccessful\n')
    elif x.status_code <= 500 or x.status_code <= 599:
        print('\n\nServer error\n')
        exit()
    time.sleep(random.randint(1,10))

    html = x.text
    soup = BeautifulSoup(html, 'lxml')

    title = soup.find('span', re.compile(r'a-size-large product-title-word-break')).text
    title = title.strip()
    df_new.loc[i, 'title'] = title

    try:
        price = soup.find('span', re.compile(r'a-price-whole')).text
        price = Decimal(sub(r'[^\d.]', '', price))
        df_new.loc[i, 'price'] = price
        
    except:
        price = soup.find('span', re.compile(r'a-offscreen')).text
        price = Decimal(sub(r'[^\d.]', '', price))
        df_new.loc[i, 'price'] = price
        
    df_new.to_csv('amazon_price_comparison.csv', index = False)

df_old = pd.read_csv('amazon_price_comparison.csv')

for i in range(len(df_old)):
    if df_old.loc[i, 'price'] == df_new.loc[i, 'price']:
        print('price has not changed')
    elif df_old.loc[i, 'price'] < df_new.loc[i, 'price']:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has increased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('amazon_price_update_comparison.csv', index = False)
    else:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has decreased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('amazon_price_update_comparison.csv', index = False)

print('\nRun End >>>')
