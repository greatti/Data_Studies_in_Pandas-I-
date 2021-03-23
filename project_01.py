# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:23:33 2021

@author: great
"""

#To start with every project in data, we import pandas and numpy, and define the max display of rows and columns:

import pandas as pd
import numpy as np 

pd.options.display.max_columns = None
pd.options.display.max_rows = None

#Then, we get our dataframe from NISPUF17.csv and we can print out the head of it 

df = pd.read_csv('NISPUF17.csv') #Please, note that the csv file need to be at the same directory as your code file, or you can copy the path
print(df.head())