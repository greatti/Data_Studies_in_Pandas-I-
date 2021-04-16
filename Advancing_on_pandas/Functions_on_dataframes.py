'''
            OBSERVATION: EVERY #### IS A PRINT STATEMENT, I RECOMMEND YOU TO FOLLOW THE 
            CLASS AND GO REMOVING THE SHARPS TO SEE THE OUTPUT
'''

import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv') #You need to put your path here
pd.options.display.max_columns = None #para nao ter limite de colunas
pd.options.display.max_rows = None #para nao ter limite de linhas
#### print(df.head())

'''
So, ultill now we did many processes one at a time, but we can use CHAINING to do all at once:
Lets get this dataframe df, use STNAME and CTYNAME as multiindexes and load the dataframe only
to data where ['SUMLEV'] == 50, and rename a column 
'''

df = (df.where(df['SUMLEV'] == 50)
    .dropna()
    .set_index(['STNAME'], ['CTYNAME'])
    .rename(columns = { 'ESTIMATESBASE2010' : 'Estimates Base 2010'}))

#### print(df.head())

'''
We can question: how fast it is to realize all this processes at once when comparad to doing one at a time?

For that we use 'timeit' library in two different functions
'''

def first_approach(): #Doing all at once in 'df'
    global df 
    return (df.where(df['SUMLEV'] == 50)
            .dropna()
            .set_index(['STNAME', 'CTYNAME'])
            .rename(columns = { 'ESTIMATESBASE2010' : 'Estimates Base 2010'}))
    
df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')
#### print(timeit.timeit(first_approach, number = 10)) #Calculate the time to run this function 10 times 

def second_approach(): #Doing one action at a time in 'df'
    new_df = df[df['SUMLEV'] == 50]
    new_df.set_index(['STNAME', 'CTYNAME'], inplace = True)
    return new_df.rename(columns = {'ESTIMATESBASE2010' : 'Estimates Base 2010'})

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')
#### print(timeit.timeit(second_approach, number = 10))

'''Apparently the second method is 4 times faster, even the first one being leaner, so, if you are heading
a big study or a big analysis, maybe it is better if you do one step at a time in terms of velocity'''

# =================================================================================================================#

''' We can clean all the variables now, because we'll explore map()

When we want to use map(), we gotta pass to it some function and some iterable. The function, then, is
applied to all the elements in this iterable and return a list of results

Map in pandas is called by 'applymap()', you need to enter a function to be applied in each cell of the 
dataframe, the result will be other dataframe 

Another way to do this is by calling only Apply

We'll practice this with census.csv, we have 5 columns of population estimate, one for each year.
It is normal if we want to create a new column just with min/max values, and 'apply()' is a good way to do it

First we need to write a function that get a line of data, find the min, find the max and return a new line
'''

import pandas as pd
import numpy as np
pd.options.display.max_columns = None #para nao ter limite de colunas
pd.options.display.max_rows = None #para nao ter limite de linhas

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')

def min_max(row):
    data = row[['POPESTIMATE2010', 
                'POPESTIMATE2011', 
                'POPESTIMATE2012', 
                'POPESTIMATE2013', 
                'POPESTIMATE2014', 
                'POPESTIMATE2015',]] 
    return pd.Series({'min' : np.min(data), 'max' : np.max(data)}) 
    #we are creating a Series with two columns:
        #min is calculating the minimum value of each row
        #max is calculating the maximum value of each row

'''the function return a Serie with two columns based on 'data' data, filtering the min and the max of each row

Now, we need to use 'Apply()' in df using min_max():

    Apply uses two parameters: 
                                -Axis: which axis is the index? 'columns' or 'rows'? 
'''

dff = df.apply(min_max, axis = 'columns').head() 
#### print(dff)
#will apply min_max() function on columns of 'df' and return a Series with this two columns only

''' What if we wanted to incorporete this two columns to census.csv? '''

def min_max2(row):
    data = row[['POPESTIMATE2010', 
                'POPESTIMATE2011', 
                'POPESTIMATE2012', 
                'POPESTIMATE2013', 
                'POPESTIMATE2014', 
                'POPESTIMATE2015',]] 
    row['max'] = np.max(data) #create a row called 'max' that is the maximum value of 'data'
    row['min'] = np.min(data) #create a row called 'min' that is the minimum value of 'data'
    
    return row #return this two new rows

dfff = df.apply(min_max2, axis = 'columns').head() 
#### print(dfff)
#will apply the function on 'df' and incorporate this columns to the dataframe

'''
All this things we did can be done in a single line using lambda function
'''

rows = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
dfmax = df.apply(lambda x: np.max(x[rows]), axis = 'columns').head() #we are applying np.max on 'rows' list of columns of df
dfmin = df.apply(lambda x: np.min(x[rows]), axis = 'columns').head()
#### print(dfmax)
#### print(dfmin)

'''
lambda: 
        -This is like a unnamed function that gets a unique variable 'x' and return
        a unique value, in this case, the maximum value of each element on the liste

apply is a cool way to go because we can use whatever function we defined previously and use whatever 
function we want with lambda

You see? In this case, we are applying on 'df' the 'lambda' function, in this case,  np.max() and np.min(), 
on the columns we specified before
'''

