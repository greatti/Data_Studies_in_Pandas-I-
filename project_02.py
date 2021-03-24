# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:22:22 2021

@author: great
"""





''' 
                 OBSERVATION:
THE PRINTS MARKED WIT #### ARE JUST FOR OBSERVATION
YOU CAN UNMARK TO SEE THE RESULTS STEP BY STEP

'''





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

#### print(df['CBF_01'].unique()) #To see that the 4 possible variables are [ 1 2 99 77] 

'''
Page 177 says: a code of 77 is used for "Don't Know" responses and a code of 99 is used for "Refused" responses
Page 110 says : 1='Yes' 2='No'

So we got it!
'''

keepcolumns = ['CBF_01', 'P_NUMFLU'] #To create a list with only this column
dfflu = df[keepcolumns]  #And pass this two columns to a new dataframe called dfflu
#### print(dfflu.head(100))

tnan = len(dfflu) #To see the number of elements in the study 
#### print(tnan) # tnan = 28465 is the total without disregarding the NaN in P_NUMFLU

'''
But let filter this dataframe for children that were fed with breastmilk, that is, ['CBF_01'] == 1
and for children that were not fed with breastmilk, that is,['CBF_01'] == 2
'''

dfflu_yes = dfflu[dfflu['CBF_01'] == 1].dropna() #This means : Filter just for [CBF_01] == 1 and drop NaN from all the columns
dfflu_no = dfflu[dfflu['CBF_01'] == 2].dropna() #This means : Filter just for ['CBF_01'] == 2 and drop NaN from all the columns
dfflu_dontknow = dfflu[dfflu['CBF_01'] == 77].dropna() #Same to dont know answers
dfflu_refuse = dfflu[dfflu['CBF_01'] == 99].dropna() #Same to refused answers

'''
A question to you think about: In this case, the NaN in ['P_NUMFLU'] are useless or they say something?
We should drop it? I will because it says nothing to our relation between variables
'''

#### print(dfflu_yes.head(10))
#### print(dfflu_no.head(10))

'''
Now what we want to discover is pretty simple: what is the medium number of doses that children that were
fed with breastmilk took, and what is the medium number of doses of those who were not fed with breastmilk?

This way we can say "oh, those who were fed needed less doses" and explore the reason of this

Lets calculate two more things: 
                                y : number of children that were fed
                                n : number of children that were not fed
'''

y = len(dfflu_yes) # y = 13291
n = len(dfflu_no) # n = 1997
dn = len(dfflu_dontknow) # dn = 42
r = len(dfflu_refuse) # r = 3
t = (y + n + dn + r) # t = 15333 (This disregard all the NaN)
#### print(y, n, dn, r, t)

y_av = np.sum(dfflu_yes['P_NUMFLU'])/y #To sum all the values from the P_NUMFLU column of dfflu_yes dataframe and divide by the number of children that were fed
n_av = np.sum(dfflu_no['P_NUMFLU'])/n #To sum all the values from the P_NUMFLU column of dfflu_no dataframe and divide by the number of children that were not fed

print(y_av, n_av) #To return a tuple of the result


'''
So all we can conclude is, children fed with breastmilk take, in average, more doses than those who arent fed.

The next part of the study is much much simpler, because it is just a complement, we will see two things: 
    
    - What is the proportion of children of each class of CBF_01? I mean, we have more children in the study 
    that were fed, that were not, that dont know....? Because the number of children in each class could
    affect the results
    
    - Of those that took the maximum number of doses, how many of them were fed with breastmilk? and of those
    that took the minimum number of doses?


We are going to quickly repeat some processes
'''

import pandas as pd
import numpy as np 

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('NISPUF17.csv')
keepcolumns = ['CBF_01', 'P_NUMFLU'] #To create a list with only this column
dfflu = df[keepcolumns]

yes = (y / t)*100
no = (n / t)*100
dontknow = (dn / t)*100
refused = (r / t)*100

print(yes, no, dontknow, refused)

'''
For the second question we need to get the our first dataframe called dfflu and filter it to the
maximum number of doses we have, which we need to see too
'''

dmin = min(dfflu['P_NUMFLU'].dropna().unique())
dmax = max(dfflu['P_NUMFLU'].dropna().unique())
#### print(dmax) # dmax = 6.0
#### print(dmin) # dmin = 0.0

dfflu_doses_max = dfflu[dfflu['P_NUMFLU'] == dmax].dropna()
#### print(dfflu_doses_max) #Only 3 children took 6 doses and this 3 children were fed with breastmilk

dfflu_doses_5 = dfflu[dfflu['P_NUMFLU'] == 5.0].dropna()
#### print(dfflu_doses_5)

dfflu_doses_min = dfflu[dfflu['P_NUMFLU'] == dmin].dropna()
#### print(dfflu_doses_min)