import pandas as pd 
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('admission.csv')
print(df.head(10)) #To see the first 10 rows at our datasheet

'''
We didnt choose a index, so pandas insert numbers to substitute, but we can define that. 
Lets get Serial No.
'''

df = pd.read_csv('admission.csv', index_col = 0) #That way the first column dissapear and the next one (Serial No.) becomes index
print(df.head(5)) 
