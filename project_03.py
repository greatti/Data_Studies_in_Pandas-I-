# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:33:17 2021

@author: great
"""

'''
For this third project we will see the relation between other three variables: 
    
    ['SEX'] that indicates the sex of the child: Male or Female
    ['HAD_CPOX'] that indicates if the child had cpox : Yes, No, Dont know, refused or missing
    ['P_NUMVRC'] that indicates the number of varicella doses 
    
But why? Because we want to see the number of children that were vaccinated but contracted CPOX
and we will do this for Male and Female

How we'll do this? filtering ['P_NUMVRC'] to greater than one dose, and then filtering again to
['HAD_CPOX'] == Yes and we will do this for Male and Female

When we do this, we will need to do the same thing to the ones who took at least one dose and
hadnt cpox

This way we can calcullate the effectivity of the vaccine, lets start then: 
    
'''

import pandas as pd
import numpy as np 

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('NISPUF17.csv')

#### print(df['SEX'].unique()) #To see all the values, 1 for male 2 for female
#### print(df['HAD_CPOX'].unique()) #2 for No, 1 for yes, 77 for dontknow and 99 for refused
#### print(df['P_NUMVRC'].unique()) 

''' Lets get just the three columns that matters '''

keepcolumns = ['SEX', 'P_NUMVRC', 'HAD_CPOX'] #To create a list with only this column
df = df[keepcolumns]  #And pass this two columns to a new dataframe called dfflu
#### print(df.head(100))