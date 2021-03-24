# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:22:22 2021

@author: great
"""

import pandas as pd
import numpy as np 

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('NISPUF17.csv')

'''
The first study we gonna do is see the relation between children that were fed by 
breast milk and number of FLU doses they took. 

For this we will use CBF_01 and P_NUMFLU

CBF_01 could be 'Yes' 'No' 'Dont know' and 'Missing'
P_NUMFLU is the number of doses for each childern
'''

print(df['CBF_01'].unique()) #To see that the 4 possible variables are [ 1 2 99 77] 

'''
Page 177 says: a code of 77 is used for "Don't Know" responses and a code of 99 is used for "Refused" responses
Page 110 says : 1='Yes' 2='No'

So we got it!
'''

keepcolumns = ['CBF_01', 'P_NUMFLU'] #To create a list with only this column
dfflu = df[keepcolumns]  #And pass this two columns to a new dataframe called dfflu
print(dfflu.head(100))

n = len(dfflu) #To see the number of elements in the study 
print(n) # n = 28465 is the total

'''
But let filter this dataframe for children that were fed with breastmilk, that is, ['CBF_01'] == 1
and for children that were not fed with breastmilk, that is,['CBF_01'] == 2
'''

dfflu_yes = dfflu[dfflu['CBF_01'] == 1].dropna() #This means : Filter just for [CBF_01] == 1 and drop NaN from all the columns
dfflu_no = dfflu[dfflu['CBF_01'] == 2].dropna() #This means : Filter just for ['CBF_01'] == 2 and drop NaN from all the columns