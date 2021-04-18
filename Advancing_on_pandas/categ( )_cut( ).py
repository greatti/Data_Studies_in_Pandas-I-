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

We can use cut(df, x) method to separate the data into groups of x elements
'''

dfcut = pd.cut(df, 10)
print(dfcut)