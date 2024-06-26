import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
tp= ['robot','human']
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.loc[data['whoAmI']!= 'human' ,'human'] = False
data.loc[data['whoAmI']!= 'robot','robot'] = False
data.loc[data['whoAmI'] == 'human', 'human'] = True 
data.loc[data['whoAmI'] == 'robot', 'robot'] = True
data = data[['human','robot']]