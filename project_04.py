# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:03:45 2021

@author: great
"""

''' 
                 OBSERVATION:
THE PRINTS MARKED WIT #### ARE JUST FOR OBSERVATION
YOU CAN UNMARK TO SEE THE RESULTS STEP BY STEP

'''

'''
This is the smaller one but it will help you a lot and make sense in the end; 
For this project we'll learn how to calculate pval and corr with scipy library
that are 2 basic operations to see the relation between variables; 
In this case we will confirm the relation between Having CPox and the number
of doses, that is, ['HAD_CPOX'] and ['P_NUMVRC']. 

corr > 0 means that an increase in ['HAD_CPOX'] (more no's) would also increase ['P_NUMVRC'] (more doses of vaccine)
corr < 0 indicates that having chickenpox is related to an increase in number of vaccine doses (more no's have relation
                                                                                                with more doses)
pval is the probability of having a relation between two columns. A small pval means that the observed correlation is
highly unlikely to occur by chance, In this case, pval should be very small (will end in e-18 indicating a very small
                                                                             number).
'''