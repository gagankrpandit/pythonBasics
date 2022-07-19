from operator import index
import pandas as pd
import re
import requests
from tqdm import tqdm

url = 'https://docs.google.com/spreadsheets/d/18sClQNUTVaQUHiHrplLFKtyfDPJfNxARKD1Sro0DuiU/edit#gid=0'
url1 = url.replace('/edit#gid=', '/export?format=csv&gid=')
col_list = ['url']
df_new = pd.read_csv(url1, usecols = col_list)

print('Run Start >>>\n')
for i in tqdm(range(len(df_new)), desc = 'progress...'):
    x = requests.get(df_new.loc[i, 'url'])
    text = x.text
    pattern = re.compile(r'(\₹)\d+\,+\d+')
    price = pattern.search(text)
    price_mo = price.group()
    price_mo = price_mo.replace('₹', '')
    price_mo = price_mo.replace(',', '')
    price_mo = float(price_mo)
    df_new.loc[i, 'price'] = price_mo
    df_new.to_csv('price_comparison.csv', index = False)

df_old = pd.read_csv('price_comparison.csv')

for i in range(len(df_old)):
    if df_old.loc[i, 'price'] == df_new.loc[i, 'price']:
        pass
    elif df_old.loc[i, 'price'] < df_new.loc[i, 'price']:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has increased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('price_update_comparison.csv', index = False)
    else:
        pctChange = ((df_new.loc[i, 'price'])-(df_old.loc[i, 'price']))/(df_old.loc[i, 'price']) * 100
        pctChange = "{:.2f}".format(pctChange)
        print(f'price has decreased {pctChange}', '%')
        df_old.loc[i, 'new price'] = df_new.loc[i, 'price']
        df_old.to_csv('price_update_comparison.csv', index = False)

print('\nRun End >>>')
