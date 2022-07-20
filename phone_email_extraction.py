import re
import pandas as pd

with open('pdf.txt') as f: # pdf text copied from a pdf file to a text file
    text = f.read()

phoneRegexObj = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
emailRegexObj = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
phone_ = phoneRegexObj.findall(text)
email_ = emailRegexObj.findall(text)

df = pd.DataFrame(phone_, columns = ['Phone'])
df['Email'] = email_
df.to_csv('contact.csv', index = False)
