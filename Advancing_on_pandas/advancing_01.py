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

''' And we can even add the left frame elements to the right frame, or the opposite '''
right_df = pd.merge(staff_df, students_df, how = 'right', left_index = True, right_index = True)
left_df = pd.merge(staff_df, students_df, how = 'left', left_index = True, right_index = True)
print(right_df)
print(left_df)

'''Notice that in the right join we have just 'students_df' elements, and in the left join we have just
'staff_df' elements

Do you remember that we had to set the indexes before merging? We dont need to do it if we use 'on' parameter

'''
join_on = pd.merge(staff_df, students_df, how = 'right', on = 'Name')
print(join_on)

''' What if we had conflict between frames?'''

staffdf = pd.DataFrame([{'Name' : 'Greatti', 'Role' : 'Programmer', 'Location' : 'Maringá'},
                         {'Name' : 'Fuzioka', 'Role' : 'Gastronomer', 'Location' : 'Maringá'},
                         {'Name' : 'Utida', 'Role' : 'Designer', 'Location' : 'São Paulo'}])

studentsdf = pd.DataFrame([{'Name' : 'Greatti', 'School' : 'UEM', 'Location' : 'Center' },
                           {'Name' : 'Fuzioka', 'School' : 'Cesu', 'Location' : 'Guedner Avenue'},
                           {'Name' : 'Currie', 'School' : 'PUC', 'Location' : 'Duque'}])

print(staffdf)
print(studentsdf)

''' We want all the information about people on staff, that is, the info in staffdf and their
info in studentsdf in case there is any student at staff '''
info_staff = pd.merge(staffdf, studentsdf, how = 'left', on = 'Name')
print(info_staff)
''' See that because we had two different columns named 'Location', Pandas atributted _x and _y sufixes '''

'''What if the first name of two people are equal but not the last name? '''

staffdf = pd.DataFrame([{'Fname' : 'Brenno', 'Lname' : 'Greatti', 'Role' : 'Programmer'}, 
                        {'Fname' : 'Larissa', 'Lname' : 'Reis', 'Role' : 'Gastronomer'}, 
                        {'Fname' : 'Leo', 'Lname' : 'Utida', 'Role' : 'Designer'}])

studentsdf = pd.DataFrame([{'Fname' : 'Brenno', 'Lname' : 'Bethe', 'School' : 'Math'}, 
                           {'Fname' : 'Joui', 'Lname' : 'Jouki', 'School' : 'Publicity'}, 
                           {'Fname' : 'Larissa', 'Lname' : 'Reis', 'School' : 'Gastronomy'}])

#Brenno Bethe and Joui Jouki arent in staffdf, but Larissa Reis is

Intersec = pd.merge(staffdf, studentsdf, how = 'inner', on = ['Fname', 'Lname'])
print(Intersec) #And now we see that the only intersection is Larissa Reis, that are on both frames in index

'''
Lets look to a lot of datasets: 
                                - MERGED2011_12_PP.csv
                                - MERGED2012_13_PP.csv
                                - MERGED2013_14_PP.csv
These are data from US Department of Education College Scorecard that have data from each US University
over the years, each CSV file is a year
'''

df2011 = pd.read_csv('MERGED2011_12_PP.csv', error_bad_lines = False) #error_bad_lines = False means that "bad lines" will be dropped
df2012 = pd.read_csv('MERGED2012_13_PP.csv', error_bad_lines = False)
df2013 = pd.read_csv('MERGED2013_14_PP.csv', error_bad_lines = False)

print(df2011.head())
print(df2012.head())
print(df2013.head())
#If we want to see the length of the dataframes:
print(len(df.2011))
print(len(df.2012))
print(len(df.2013))

#We can now create a list with the three dataframes to concatenate them

frames = [df2011, df2012, df2013]
conc = pd.concat(frames)

