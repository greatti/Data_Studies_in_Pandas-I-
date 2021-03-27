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

''' Now we filter to just the ones who had and who had not '''

df_yes = df[df['HAD_CPOX'] == 1].dropna()
df_no = df[df['HAD_CPOX'] == 2].dropna()

''' And now we filter to who took at least one dose and none dose and had cpox
Then, we do the same thing to who had not cpox
'''

df_yes_one = df_yes[df_yes['P_NUMVRC'] > 0.0].dropna()
df_yes_none = df_yes[df_yes['P_NUMVRC'] == 0.0].dropna()

df_no_one = df_no[df_no['P_NUMVRC'] > 0.0].dropna()
df_no_none = df_no[df_no['P_NUMVRC'] == 0.0].dropna()

#### (df_yes_one.head())
#### print(df_yes_none.head())
#### print(df_no_one.head())
#### print(df_no_none.head())

''' To end this, we will create 8 more dataframes, because each one of this last dataframes
we have to separate in male and female '''

df_yes_one_m = df_yes_one[df_yes_one['SEX'] == 1].dropna() #had cpox, at least one dose, male
df_yes_one_f = df_yes_one[df_yes_one['SEX'] == 2].dropna() #had cpox, at least one dose, female

df_yes_none_m = df_yes_none[df_yes_none['SEX'] == 1].dropna() #had cpox, no doses, male
df_yes_none_f = df_yes_none[df_yes_none['SEX'] == 2].dropna() #had cpox, no doses, female

df_no_one_m = df_no_one[df_no_one['SEX'] == 1].dropna() #hadnt cpox, at least one dose, male
df_no_one_f = df_no_one[df_no_one['SEX'] == 2].dropna() #hadnt cpox, at least one dose, female

df_no_none_m = df_no_none[df_no_none['SEX'] == 1].dropna() #hadnt cpox, no doses, male
df_no_none_f = df_no_none[df_no_none['SEX'] == 2].dropna() #hadnt cpox, no doses, female

#### print(df_yes_one_m.head(20))
#### print(df_yes_one_f.head(20))
#### print(df_yes_none_m.head())
#### print(df_yes_none_f.head())
#### print(df_no_one_m.head())
#### print(df_no_one_f.head())
#### print(df_no_none_m.head())
#### print(df_no_none_f.head())

''' And now we have to count the number of elements '''

t1 = len(df_yes_one_m)
t2 = len(df_yes_one_f)
t3 = len(df_yes_none_m)
t4 = len(df_yes_none_f)
t5 = len(df_no_one_m)
t6 = len(df_no_one_f)
t7 = len(df_no_none_m)
t8 = len(df_no_none_f)
t = (t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8)

print(t1, t2, t3, t4, t5, t6, t7, t8)

'''
OK now we have all we need, so we can create a dictionary to calculate:
    
    The percentage of man that had cpox but took at least one dose
    The percentage of man that had cpox but did not took at least one dose
    The percentage of man that hadnt cpox and took at least one dose
    The percentage of man that hadnt cpox and did not took at least one dose

    The percentage of woman that had cpox but took at least one dose
    The percentage of woman that had cpox but did not took at least one dose
    The percentage of woman that hadnt cpox and took at least one dose
    The percentage of woman that hadnt cpox and did not took at least one dose
'''




































