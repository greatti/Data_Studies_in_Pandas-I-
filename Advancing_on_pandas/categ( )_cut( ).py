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