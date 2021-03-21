import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

'''
Lets work now with multindex dataframes
To train that we will import 'census.csv'
'''

df = pd.read_csv('census.csv') #This table is too big, we have 100columns

'''
SUMLEV is a column that defines only two values: 40 and 50 
We can print out the values from a column using unique()
'''

print(df['SUMLEV'].unique()) #will print 40 and 50

'''
Lets filter this sheet to elements that SUMLEV == 50
'''

df = df[df['SUMLEV'] == 50] #Will filter the elements where 'SUMLEV' == 50 and dropNa
print(df.head()) #To confirm

'''
We have too much information in this dataframe, so lets reduce this
'''

keepcolumns = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 
                   'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011','POPESTIMATE2012',
                   'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
            
'''
And now we push that columns to the dataframe and set 2 indexes
'''

df = df[keepcolumns]
df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head())

'''
Because of that multiindex, when you print the dataframe its wasy to notice that it is grouped by
states, and inside each state we have the citys, and for every city we have all the information

See how it is easy to found a info about a city: 
'''

print(df.loc[[('Michigan', 'Washtenaw County'), 
('Michigan', 'Wayne County')]])

# ============================================== grades.csv ============================================== #

'''
Lets switch the dataset to 'class_grades.csv' 
There is NaN data in this datasheet, so we can create a boolean_mask using isnull() 
that identifies where are the NaN
'''

mask = df.isnull() #And now we have a dataframe with True and False, we can use dropna() to remove the NaN's
print(df.dropna()) #Now if we print(df) its visible that the NaN are not in there anymore, or we can substitute NaN to -1
df = df.fillna(-1, inplace = True) #And this way we dont have NaN but we have -1 inplace

# ============================================ log.csv ============================================ #

import pandas as pd
df = pd.read_csv('log.csv')
pd.options.display.max_columns = None
pd.options.display.max_rows = None

'''
Lets organize this datasheet seting 'time' to index
in crescent order
'''

df = df.set_index(['time'])
df = df.sort_index()

'''
More than one user can use the system at the same time, so we
need to define a multiindex with user and time and del ['index']
'''

df = df.reset_index()
df = df.set_index(['time', 'user'])

'''
If you print this last thing we've done, its noticible that there is a lot of NaN.
Lets fill the NaN with something using ffill()

Using ffil(), all the 'paused' values will be set in False, thats because all the NaN 
are substituted vertically by the last one. 

It happens the same for 'volume' values 10.0
'''

df = df.fillna(method = 'ffill', axis = 0, inplace = False)
#The values will not be permanently
#The values substituted are columns
#The method is by getting the last one vertically

'''
We can substitute some values with one choosen 
'''

df = df.replace([10,5], ['max', 'medium'])
print(df.head(10)) #To verify

'''
This will substitute all the 10.0 with max and all the 5.0 with medium
Lets detect in the video column all the data that ends with .html and 
substitute for 'webpage' 

That is, any number of characteres that ends with .html
'''

df = df.replace(to_replace = '.*.html$', value ='webpage', regex = True)









