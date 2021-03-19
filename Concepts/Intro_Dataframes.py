import pandas as pd 
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('admission.csv')
print(df.head(10)) #To see the first 10 rows at our datasheet

'''
We didnt choose a index, so pandas insert numbers to substitute, but we can define that. 
Lets get Serial No.
'''

df = pd.read_csv('admission.csv', index_col = 0) #That way the first column dissapear and the next one (Serial No.) becomes index
print(df.head(5))

'''
Lets rename some columns of the dataframe using rename() creating a dictionary with keys:old names and values: new names
'''

new_df = df.rename(columns = {'GRE Score' : 'GRE Score', 
                              'TOEFL Score' : 'TOEFL Score', 
                              'University Rating' : 'University Rating', 
                              'SOP' : 'Statement of Purpose', 
                              'LOR' : 'Letter of Recommendation', 
                              'CGPA' : 'CGPA', 
                              'Research' : 'Research', 
                              'Chance of Admit' : 'Chance of Admit'}) #You can see that we had to rename ALL the columns    

print(new_df.head(5)) 

'''
See that LOR is the same but SOP changed? Why? Lets use .columns() to see all the columns in the new_df
'''

print(new_df.columns) #That way we observe that 'Chance of Admit' and 'LOR' have a whitespace in the end, so we wrote it wrong

new_df = new_df.rename(columns = {'LOR ' : 'Letter of Recommendation'}) #That way we change just the name of this column

print(new_df.head())
print(new_df.columns)

'''
Lets agree, this is too fragile, because we cant spend time seeing if there is a whitespace or not in all the columns.
strip() is a function that clean the names and rename it.
'''

new_df = new_df.rename(mapper = str.strip, axis = 'columns')
print(new_df.head())

'''
And lets do this for df too 
'''

df = df.rename(mapper = str.strip, axis = 'columns')  #This will clean the whitespaces in all columns of df
print(df.columns)
print(df.head())
df = df.rename(columns = { 'LOR' : 'Letter of Recommendation', 'SOP' : 'Statement of Purpose'}) #Now we know that we dont have any whitespaces

print(df.head()) #To confirm
print(df.columns) #To confirm

'''
What if we wanna change ALL the column names?
First we gotta create a list with all the column names, then, apply a list comprehension: 
'''

colunas = list(df.columns) #Creating a list
colunas = [x.lower().strip() for x in colunas] #Applying a list comprehension
df.columns = colunas 
print(df.columns)
'''
This way we are applying a function to the columns, we can to this with uppercase too
'''

# ======================================== FROM HERE YOU CAN CLEAN YOUR VARIABLES ======================================== #

import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('admission.csv', index_col = 0) #To set the index to [Serial No.]
df.columns = [x.lower().strip() for x in df.columns] #To remove the whitespaces and keep all the words in lowercase
print(df.head()) #To confirm
print(df.columns) #To confirm
print(df['chance of admit']) #This way we can see ALL the data from ['chance of admit'] column 

'''
Lets do our first cleaning in data: Lets say that we want those data that ['chance of admit'] > 0.7

First we gotta create another dataframe build from 'df' but filtered to ['chance of admit'] > 0.7
'''

admit_mask = df['chance of admit'] > 0.7 #That will say TRUE or FALSE for the condition
print(admit_mask.head(10))

'''
Now we apply the Admit_Mask to our df, and it will return just the data that fulfill the condition using where()
'''

print(df.where(admit_mask).head(10)) 

'''
But notice that for those data where the condition dont apply, returns 'NaN', what if we want to exclude them?
For that we use dropna() 
'''

print(df.where(admit_mask).dropna().head(10))

'''
where().dropna() is the same as other function: df[df]
'''

print(df[df['chance of admit'] > 0.7].head(10))

'''
That is: df[df[]] is the same as where()dropna()
'''



