import pandas as pd
import numpy as np
df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/housing.csv')

#### print(df.head())
#### print(df.columns)

''' lets set two indexes : "cancellation_policy", "review_scores_value" '''

df = df.set_index(['cancellation_policy', 'review_scores_value']) #remember that this is a multiindex
#### print(df.head())

for group, frame in df.groupby(level = (0,1)): 
    print(group)

''' "level" is a parameter that tells groupby( ) from which index we want to group by, and, in this case, we want both 
this will iterate into the indexes and print de tuple the values of both the indexes

lets create a function that separates a data if the review score is 10.0
'''

def rev_10(item): 
    if item[1] == 10.0: 
        return(item[0], str(10.0))
    else: 
        return(item[0], 'not 10.0')
for group, frame in df.groupby(by = rev_10) : 
    print(group)
''' This function, applied on the dataframe, will search on item[1], that is, the second index and for those where the 
value is equal to 10.0 it will return what is the cancellation_Policy of it (item[0]) and 10.0, for those where the value 
is not equal to 10.0 it will also return what is the cancellation_Policy of it and 'not 10.0'

Apparently, for all types of 'cancellation_policies' exists 10.0s and not 10.0s 
'''

#####################  AGGREGATION #########################

df = df.reset_index()
df.groupby('cancellation_policy').agg({'review_scores_value' : np.average}) 

'''It should return a Serie of averages calculated on 'review_scores_value', but remember that this dataframe have NaN
and this operation dont ignore them'''

df.groupby('cancellation_policy').agg({'review_scores_value' : np.nanmean})

'''We substitute np.average with np.nanmean, because this operation ignore NaN 

This is just an example, but we dont need necessarily to associate just one function, we can use a lot of them, and
we can associate to a lot of columns too! '''

#### print(df.groupby('cancellation_policy').agg({'review_scores_value' : (np.nanmean, np.nanstd),
                                       #### 'reviews_per_month' : np.nanmean}))

'''
In this case we are applying two functions to 'review_scores_value' and one to 'reviews_per_month', the print statement 
should return the result of this three functions when grouped by cancellation_plociy

The results show, for example, that super_strict_30 types have a much much lower number of reviews per month in average
and that only happens because we could separate this results using groupby, to apply in a hole group, do you see how this 
is different from index?

by the way, we didnt even defined an index!

Notice that Agg( ) method return for us a unique value each column
'''

#transform( ) is a function that return an object that have same size as the group
cols = ['cancellation_policy', 'review_scores_value'] #we'll modify 'df' to stay with just these two columns
transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)
#### print(transform_df.head(20))

''' All the elements that have the same group will have the same value too, in that case, it is the average of each gorup.
that means we created a new dataframe called transform_df where every value represent the average of its 'cancellation_po-
licy' group

What if we wanted to join this column to the original dataframe now? We can use merge( ) 
'''

transform_df.rename({'review_scores_value' : 'mean_review_score'}, axis = 'columns', inplace = True) 
#This is known, we are just renaming a column of transform_df 

df_merge = pd.merge(df, transform_df, how = 'outer', left_index = True, right_index = True)
#### print(df_merge.head(20)) 

# IT WORKS!!!