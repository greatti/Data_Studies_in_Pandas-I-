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

