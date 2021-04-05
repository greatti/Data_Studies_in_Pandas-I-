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

