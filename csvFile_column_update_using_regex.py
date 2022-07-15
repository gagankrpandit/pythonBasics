import time
start = time.process_time()
import re
import pandas as pd
data = pd.read_csv('consumer_complaints - Copy.csv',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

for i in range(len(data)):
    try:
        regex = re.compile(r'\d\d/\d\d/\d\d\d\d')
        mo = regex.search(str(data.loc[i, 'date_received']))
        mogrp = mo.string
        dd = mogrp[3:5]
        mm = mogrp[:2]
        yyyy = mogrp[-4:]
        date_ = dd + '-' + mm + '-' + yyyy
        data.loc[i, 'date_received'] = date_
        data.to_csv('consumer_complaints - Copy.csv', index=False)
    except:
        pass

print(f'Done! The loop ran {i} times!')
print(time.process_time() - start)
