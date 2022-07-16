from tqdm import tqdm
import pandas as pd
col_list = ['date_received', 'product', 'issue', 'company',
       'state', 'zipcode','submitted_via', 'date_sent_to_company', 'company_response_to_consumer',
       'timely_response', 'consumer_disputed?', 'complaint_id']
dateCol = ['date_received', 'date_sent_to_company']
dtypes = {'product':'str', 'issue':'str', 'company':'str',
       'state':'str', 'zipcode':'str','submitted_via':'str','company_response_to_consumer':'str', 
       'timely_response':'str', 'consumer_disputed?':'str', 
       'complaint_id':'str'}

data = pd.read_csv("consumer_complaints - Copy.csv", usecols = col_list, dtype = dtypes, 
parse_dates = dateCol) #parse_date to clean and update date columns
data.to_csv('consumer_complaints - python.csv', index = False)
