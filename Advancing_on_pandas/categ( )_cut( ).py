import pandas as pd 

''' 
What if we have a dataframe with class grades and obtain just those that the grade is greater than B+ for example, 
but essentialy B+ ou A+ are the same, cause they are both string with no value 
'''

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'], index = ['excellent','excellent', 'excellent', 'good', 'good', 'good', 
                  'ok', 'ok', 'ok', 'poor', 'poor'],
                columns = ['Grades'])
#### print(df) 

#Now we'll set the 'Grades' column into categorical type 
df['Grades'].astype('category')
#### print(df)

''' but if we want to determine which students had grade greater than A, than it must exist an order
using pandas.Categorical( ) '''

my_categories = pd.CategoricalDtype(categories = ['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'], ordered = True)
grades = df['Grades'].astype(my_categories) #creating a grades dataframe applying the categorical type
#### print(grades)

#This way we define what are the values, in this case, are the elements of the column
#Categorial = [] defines the ordem

print(grades[grades > 'C']) #we can now filter 'grades' because this column is categorical and ordered

'''
we'll now create a column that say if the element is in ou out of a group determined by a condition, and 
the column will use boolean variables to express this information

to do this we will use get_dummies method 
'''

import pandas as pd
import numpy as np 

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')
df = df[df['SUMLEV'] == 50]
#### print(df.head(15))

df = df.set_index('STNAME').groupby(level = 0)['CENSUS2010POP'].agg(np.average) 
#### print(df)

'''
our dataframe is now super reduced, because we defined the STATE NAME as index and calculated the average over the 
2010 POPULATION in each state

We can use cut(df, x) method to separate the data into x bins of equal sizing, For example, cut could convert ages
to groups of age ranges.
'''

dfcut = pd.cut(df, 10)
#### print(dfcut)

###### PIVOT_TABLES ######

'''
Pivot tables is a way of sumarizing data in a dataframe by a specific motive:
'''

import pandas as pd 
import numpy as np
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/cwurData.csv')
#### print(df.head())

''' lets first create a new column, where if the university rank is 01-101, it is classified as first tier
if the university rank is 102-202 it is classified as second tier
if the univerity rank is 203-303 it is classified as third tier
the other are fourth rank

reading this you can imagine the function to do this, right? It is a if function that returns which tier
depending on rank 
'''

def create_category(ranking): 
    if (ranking >=1) & (ranking <=101):
        return 'FirstTier'
    if (ranking >101) & (ranking <=202): 
        return 'SecondTier' 
    if (ranking > 201) & (ranking <=303):
        return 'ThirdTier'
    else:
        return 'FourthTier'

''' To apply this function we dont have any problem, we'll use apply( ) with lambda '''

df['Tier'] = df['world_rank'].apply(lambda x: create_category(x))
#### print(df['Tier'].head(30)) #lets see this column, it seems it is already organized by order of tier

''' Lets suppose we want now to see the relationship between Tier and Country in terms of Score

values = Score
index = country
columns = rank_level '''

dfpiv = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean])
#### print(dfpiv.head(30))

'''
basically, what are we doing? We are getting the mean value (function) of 'Score'(values) in each Tier(columns)
of each country(index)

You noticed that we have NaN data? That means, for example, that Argentina dont have 'Score' values to apply the 
function in this classification (Tier)

pivot.table( ) isnt limited to one function, you can assign one or more: 
'''

dfpivt = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean, np.max]).head()
#### print(dfpivt)

dfpivtma = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean, np.max], margins = True)
#margins = True show the superior limit 
print(dfpivtma)