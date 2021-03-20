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


