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

# ================================ presidents.csv ================================ #

import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('presidents.csv', index_col = 0)

'''
In this csv file we have a lot of information about all the presidents of USA in crescent order
of election

Lets clean the column names
'''
df = df.rename(mapper = str.strip, axis = 'columns') #Remember that this will remove the whitespaces from the columns

colunas = list(df.columns) #To create a list with the columns
print(colunas) 

colunas = [x.lower().strip() for x in colunas] #To remove all the whitespaces and become lowercase
df.columns = colunas #to transform the list 'colunas' to columns in dataframes

'''
Lets say we now want to cut the president names and split into first and last names. 
We gotta create a function that recognizes the first and last names
'''

def splitname(row):
    row['first'] = row['president'].split(' ')[0]
    row['last'] = row['president'].split(' ')[-1]
    return row

'''
And now we apply this function to df and del the ['president'] column
Then we set index to ['first'] and ['last']
'''

df = df.apply(splitname, axis = 'columns')
del df['president']
df = df.set_index(['first', 'last'])

'''
We can do the same thing with REGEXES
'''

pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('presidents.csv', index_col = 0)
df = df.rename(mapper = str.strip, axis = 'columns')
colunas = list(df.columns) #para criar uma lista com os nomes das colunas do dataframe
colunas = [x.lower().strip() for x in colunas] #isso vai deixar tudo minusculo E retirar whitespaces
df.columns = colunas

'''
First we define a pattern to follow in regex: 
In this case, we wanna get the first and last word of 'presidents'
'''
pattern = '(^[\w]*)(?:.* )([\w]*$)'

'''
first : the start of the string, any chacactere, in any quantity followed by a whitespace
second: we dont want it to return, any number of charactere followed by a whitespace
last: any number of charactere at the end of the string 
'''

pattern = '(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)' #This is to name the groups
names = df['president'].str.extract(pattern).head() #To create two columns based on df['president']

''' If we print this out, we'll only get the two columns, so we gotta add this to our df '''

df['First'] = names['First']
df['Last'] = names['Last']

''' and then set this to multiindex '''

df = df.set_index(['First', 'Last'])

'''
If we analayze the dataframe we see that the column ['born'] is a very 
messy column, lets clean it: 

we will start with excluding all that dont follow the pattern month/day/year 
'''

df['born'] = df['born'].str.extract('([\w]{3} [\w]{1,2}, [\w]{4})')

'''
That is saying : any characteres of 3 in length, followed by a whitespace, followed by 
any characteres of 1 or 2 in length, followed by a comma, followed by a whitespace, followed
by any characteres of 4 in length

If we want to organize more, we can use .to_datetime()
'''

df['born'] = pd.to_datetime(df['born'])

'''
To end this, lets say we want to organize this by the crescent age 
'''

df = df.reset_index()
df = df.set_index(['age atstart of presidency'])
df = df.sort_index()

print(df.head(10)) # to confirm














