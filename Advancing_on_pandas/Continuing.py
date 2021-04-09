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
print(df[['CTYNAME', 'STNAME', 'REGION']].head(20))


