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

We can use cut(df, x) method to separate the data into x bins of equal sizing, For example, cut could convert ages
to groups of age ranges.
'''

dfcut = pd.cut(df, 10)
#### print(dfcut)

###### PIVOT_TABLES ######

'''
Pivot tables is a way of sumarizing data in a dataframe by a specific motive:
'''

import pandas as pd 
import numpy as np
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/cwurData.csv')
#### print(df.head())

''' lets first create a new column, where if the university rank is 01-101, it is classified as first tier
if the university rank is 102-202 it is classified as second tier
if the univerity rank is 203-303 it is classified as third tier
the other are fourth rank

reading this you can imagine the function to do this, right? It is a if function that returns which tier
depending on rank 
'''

def create_category(ranking): 
    if (ranking >=1) & (ranking <=101):
        return 'FirstTier'
    if (ranking >101) & (ranking <=202): 
        return 'SecondTier' 
    if (ranking > 201) & (ranking <=303):
        return 'ThirdTier'
    else:
        return 'FourthTier'

''' To apply this function we dont have any problem, we'll use apply( ) with lambda '''

df['Tier'] = df['world_rank'].apply(lambda x: create_category(x))
#### print(df['Tier'].head(30)) #lets see this column, it seems it is already organized by order of tier

''' Lets suppose we want now to see the relationship between Tier and Country in terms of Score

values = Score
index = country
columns = rank_level '''

dfpiv = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean])
#### print(dfpiv.head(30))

'''
basically, what are we doing? We are getting the mean value (function) of 'Score'(values) in each Tier(columns)
of each country(index)

You noticed that we have NaN data? That means, for example, that Argentina dont have 'Score' values to apply the 
function in this classification (Tier)

pivot.table( ) isnt limited to one function, you can assign one or more: 
'''

dfpivt = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean, np.max]).head()
#### print(dfpivt)

new_df = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean, np.max], margins = True)
#margins = True show the superior limit 
#### print(new_df)

#### print(new_df.index) 
#### print(new_df.columns)

#You see there is two leves of columns? ['mean', 'amax'] and ['FirstTier', 'SecondTier', 'ThirdTier', 'FourthTier']
 
new_df_mf = new_df['mean']['FirstTier'] #this way we are getting just ONE column: the mean AND FirstTear column
#### print(new_df_mf.head(15))

'''
Now that we have just one column that shows the mean value of FirstTier in each country, how can we get the best mean value
of all the countries? Using idxmax( ) 

Return index of first occurrence of maximum over requested axis. NA/null values are excluded.
'''

BEST_country = new_df_mf.idxmax()
#### print(BEST_country) 

dfs = df.pivot_table(values = 'score', index = 'country', columns = 'Tier', aggfunc = [np.mean, np.max], margins = True)
#### print(dfs.head()) #lets redefine

''' 
Lets use now stack( ) method 
'''

dfs = dfs.stack()
#### print(dfs.head(20))

''' 
You see that, this way, we dont have NaN? Because stack( ) puts 'country' as indexes, calculate the mean and max values
over 'score' values in each 'Tier' column, but it print just those that arent NaN
'''

######## TIMESTAMP ########

''' 
timestamp is a pandas function associated to time in pandas library, but it isnt the only one, we have basically four: 
- timestamp
- datatimeindex
- period
- periodindex

the first one associates values with points in space
'''

#### print(pd.Timestamp('9/1/2019 10:05AM')) # d/m/y h/m/AMorPM
#### print(pd.Timestamp(2019, 12, 20, 0, 0)) # y/m/d h/m/s

'''
pandas have a function called isaweekday( ) that shows the day of the week 
1: segunda
7: domingo
'''

#### print(pd.Timestamp(2019, 12, 20, 0, 0).isoweekday())

'''
Or we can get one information at a time calling .second or .minute etc
'''

#### print(pd.Timestamp(2019, 12, 20, 5, 2, 23).second)

'''
Now, what if we wanted to get a period of time? Then we could use Period( )
'''

#### print(pd.Period('1/2016')) # Mounth / Year
#### print(pd.Period('3/5/2016')) # Mounth / Day / Year

#### print(pd.Period('1/2016') + 1) #will return fev
#### print(pd.Period('3/5/2016') + 1) #will return day 6

########## DATETIMEINDEX and PERIODINDEX ###########

'''
lets use timestamp( ) of days one, two and three of september of 2016 to create a Serie and define them as index
'''

t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#### #print(t1)
#### print(type(t1.index)) # DatetimeIndex type

t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
#### print(t2)


d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16'] #we'll set a list of different forms to write dates
ts3 = pd.DataFrame(np.random.randint(10,100,(4,2)), index = d1, columns = list('ab'))

#### print(ts3)

''' using pandas.to_datetime it'll try to convert all those types of dates to DateTime and put them in a 
specific format '''

ts3.index = pd.to_datetime(ts3.index)
#### print(ts3) #now its fixed!

'''
when using to_datetime we can pass dayfirst = True argument to get the european model 
'''

#### print(pd.to_datetime('4.7.12', dayfirst = True))

##############################     TIMEDELTAS      #####################################

''' timedelta is a difference between datatimes '''

delta = pd.Timestamp('1/17/2019') - pd.Timestamp('9/1/2016') 
#### print(type(delta)) #timedelta object
#### print(delta)

''' Using timestamp we can see the date when summing days and hours '''

date = pd.Timestamp('9/2/2016 8:10AM')
new_date = date + pd.Timedelta('12D 3H') #after 12 days and 3 hours
#### print(new_date)

##########################      OFFSET     ################################

''' is a function that have some specific rules very usefull '''

#### print(pd.Timestamp('9/4/2016') + pd.offsets.Week()) #will add 7 days
#### print(pd.Timestamp('9/4/2016') + pd.offsets.MonthEnd()) #will add the number of days necessary to go to the end of the month

''' how can we work with dates properly? 

Lets suppose we have to look for 9 datas collected twice a week, every sunday, starting from october 2016
Using date_range( ) we specify a START, a ENDDATE, a period and a frequency
'''

dates = pd.date_range('10-01-2016', periods = 9, freq = '2W-SUN') # W2-SUN is twice a week every sunday
#### print(dates)

# https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases to see frequency aliases

''' lets generate a random dataframe that for now means nothing '''
df = pd.DataFrame({'Count 1' : 100 + np.random.randint(-5, 10, 9).cumsum(),
                   'Count 2' : 120 + np.random.randint(-5, 10, 9).cumsum()}, 
    index = dates)
print(len(df))
#### print(df)

''' to verify the week day we know we have to use weekday_name( ) '''

wd = df.index.day_name()
#### print(wd) #we see its all correct, because we wanted the days to be sundays, right?

''' lets use now pandas.dataframe.diff( ) to see the difference between datas '''

dif = df.diff()
#### print(dif)

''' What if we wanted to count how many different years or months there is in our dataframe? 
Then we should use resample( ) 

to use resample( ) the object must have datetime-like index
'''

months = df.resample('M').mean() #we are calculating the mean value of all the elements that have the same month
years = df.resample('Y').mean() #we are calculating the means value of all the elements that have the same year

#### print(months, '\n') #should return a dataframe with 4 elements
#### print(years, '\n') #should return a dataframe with 2 element

