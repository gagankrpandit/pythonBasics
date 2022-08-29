# Generate password using diceware dictionary

import random

with open('diceware.txt', 'r') as f:
        diceware_words = f.read()
listt = diceware_words.split('\n')

x = []
for i in range(len(listt)):
        x.append(listt[i].split('\t'))

diceware_dict = {}
for i in range(len(x)):
        for j in range(0, len(x[i]), 2):
                diceware_dict[x[i][j]] = x[i][j+1] 

def phrases(num):
        keys = []
        for i in range(num):
                values = str(random.randint(1,5))+str(random.randint(1,5))+str(random.randint(1,5))+str(random.randint(1,5))+str(random.randint(1,5))
                keys.append(values)
        
        pswrd = ''
        for i in range(len(keys)):    
                if keys[i] in diceware_dict.keys():
                        password = pswrd + diceware_dict[keys[i]]
                        # print('Here is your password: ', end='')
                        print(password, end='')        

num = int(input('How many phrases you want in your password: '))
phrases(num)
