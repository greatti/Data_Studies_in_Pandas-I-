import pandas as pd 
pd.options.display.max_columns = None
pd.options.display.max_rows = None

'''
we'll first create two DataFrames to work with, one called Staff and the other called Students
'''

staff_df = pd.DataFrame([{'Name' : 'Greatti', 'Role' : 'Programmer'}, 
                         {'Name' : 'Fuzioka', 'Role' : 'Gastronomer'}, 
                         {'Name' : 'Lewis', 'Role' : 'Writer'}])
                        
students_df = pd.DataFrame([{'Name' : 'Greatti', 'School' : 'UEM'},
                            {'Name' : 'Fuzioka', 'School' : 'Cesu'},
                            {'Name' : 'Utida', 'School' : 'USP'}])

''' And now we'll set 'Name' as index, because we want to join this two, notice that 'Utida' and 'Lewis' are 
not in both dataframes'''

staff_df = staff_df.set_index('Name')
students_df = students_df.set_index('Name')

print(staff_df)
print(students_df)

'''Lets merge it using merge():
merge() is a function that join two dataframes on columns or indexes
Arguments of merge() method can be found in https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge
and i cannot explain all of them in here, just the ones i'll use
'''

outer_df = pd.merge(staff_df, students_df, how = 'outer', left_index = True, right_index = True)
'''Lets explain all of this: 
merge is a function that join two dataframes, as we can see, in this case, the first two arguments; 
'how' parameter is the method, and 'outer' represent that we'll use keys from both frames
'left_index' is a parameter that ask if we want to use the index of the first frame, in this case is True
'right_index' same as left
'''
print(outer_df) #You need to observe that Lewis is in ['Role'] but not in ['School'], and the same happens to Utida

'''
If we wanted just the data that are in both frames, than we do a inner join, and we wxpect to stay with just
two rows and no missing values
'''
inner_df = pd.merge(staff_df, students_df, how = 'inner', left_index = True, right_index = True)
print(inner_df)