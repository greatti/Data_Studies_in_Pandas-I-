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