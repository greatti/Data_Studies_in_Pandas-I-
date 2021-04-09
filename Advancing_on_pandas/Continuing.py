'''
            OBSERVATION: EVERY #### IS A PRINT STATEMENT, I RECOMMEND YOU TO FOLLOW THE 
            CLASS AND GO REMOVING THE SHARPS TO SEE THE OUTPUT
'''

'''
Lets say we want to get all the data from STNAME in df and separate it in regions
    - Northeast
    - Midweast
    - South
    - West
'''
import pandas as pd
df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')

def get_state_region(x): 
    northeast = ['Connecticut', 'Maine', 'Massachussetts', 'New Hampshire', 'Rhode Island', 
                 'Vermont', 'New York', 'New Jersey', 'Pennsylvania']
    midwest = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin', 'Iowa', 'Kansas', 
               'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota']
    south = ['Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 
             'Virginia', 'District of Columbia', 'West Virginia', 'Alabama', 'Kentucky', 
             'Mississippi', 'Tenessee', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
    west = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Utah', 
            'Wyoming', 'Alaska', 'California', 'Hawaii', 'Oregon', 'Whashington']
    
    #This is separating each State in 4 regions

    if x in northeast:
        return 'Northeast'
    elif x in midwest:
        return 'Midwest'
    elif x in south:
        return 'South'
    elif x in west:        
        return 'West'
    
df['REGION'] = df['STNAME'].apply(lambda x: get_state_region(x)) 
#Define a REGION column that gets STNAME column on 'df' and apply get_state_region() function
#### print(df[['CTYNAME', 'STNAME', 'REGION']].head(20))


# =========================Lets reset all the data============================= #

import pandas as pd 
import numpy as np

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv')
df = df[df['SUMLEV'] == 50]

#Remember when we used unique() function to get all the data in a single array? Lets see how many states there is

Lstate = df['STNAME'].unique()
#### print(Lstate)

'''
To the elements in Lstate array, we'll get the average of population in 2010 in each state on ['STNAME'] column
'''
for state in Lstate:
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    #### print('counties in ' + state + ' have an average population of ' +str(avg))

for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    #### print('counties in ' + group + ' have an average population of ' +str(avg))

    ''' This will group df by state ('STNAME') and calculate the average in every state with using frames'''

#Lets create a function where we can see how many data there is in each group we define

df = df.set_index('STNAME') #setting STNAME to index

def set_batch_number(item):
    if item[0] < 'M': #If the first word of 'item' is M, return the integer 0
        return 0 
    if item[0] <'Q':  #If the first word of 'item' is Q, return the integer 1
        return 1
    return 2 #If it isnt M or Q, return the integer 2

for group, frame in df.groupby(set_batch_number): #We groupby the dataframe using the function especification
    #### print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')