# An introduction to Pandas library (Python) -- with projects!! 

<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

<details><summary>VERSIONS</summary>
<p>

```python
import pandas as pd
import numpy as np
print(pd.__version__) #To see what is your version of Pandas in Python
print(np.__version__) #To see what is your version of Numpy in Python
```
#### PYTHON : 3.9.2
#### PANDAS : 1.2.1
#### NUMPY : 1.19.2
</p>
</details>

<hr>

This is the first project of a study in Pandas library, the objective is one day we reach a professional data analysis level. Today, when im writing this (03/21/21), i finished the first part of the concepts, and you can find this in [Intro_to_pandas](https://github.com/greatti/Imunization/tree/main/Concepts), then follow this explanations: 


+ Intro_to_pandas
  - Dataframes_Multiindex.py **Explains more complexes operations of dataframes in pandas**
  - Intro_Dataframes.py **Explains the base of dataframes in pandas**
  - Admission.csv **One of the csv's used in python files**
  - census.csv **One of the csv's used in python files**
  - class_grades.csv **One of the csv's used in python files**
  - log.csv **One of the csv's used in python files**
  - presidents.csv **One of the csv's used in python files**
+ NIS-PUF17-DUG.pdf **PDF explaining all the variables in the project**
+ NISPUF17.csv **database of the project**
+ PieChart(p3).png **piechart of project_03**
+ project_01.py **the first project**
+ project_02.py **the second project**
+ project_03.py **the third project**

<hr>

### FIRST PROJECT ( [project_01](https://github.com/greatti/Data_studies/blob/main/project_01.py) )

<details><summary>DESCRIPTION</summary>
<p>

This first project is just an introduction to the next projects, you can work and modify it but we dont have much to explore, is just for understanding. 
So lets start to discuss this: The first big question to start this is "What is the proportion of children in NISPUF17.csv who had a mother with the education levels equal to less than high school, equals to high school, more than high school but not a college graduate and equals to college degree. The problem is that the csv file is too big and we dont have ANY IDEA of what all of that variables means, so we need to search in NIS-PUF17-DUG.pdf something to discover, and that is a part of the work of a data scientist too.

Page 55 says: "The age, education level, and marital status of the mother of the child are
stored in variables M_AGEGRP2, EDUC1, and MARITAL2 (married vs. not married), with missing
values imputed."

That means that our mother education level is stored in EDUC1 variable, and that is confirmed in page 51:

+ EDUC1 – education of the mother
  - Less than 12 years
  - 12 years
  - More than 12 years, not a college graduate
  - College graduate

Now we know what to do, we just need to use 'EDUC1' column, separate the education level in order, count how many there is of each type, count the total and divide each type for the total

In project_01 i did all of that explaining all of the process, but if you want a more concise code, see the follow code where i define a function, but i only recommend reading this when you have already read the original project_01.

```python
def proportion_of_education():
    import pandas as pd
    import numpy as np
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    df = pd.read_csv('NISPUF17.csv')
    MOM = df['EDUC1']
    mom = np.sort(MOM.values)

    prop = {'less than high school': 0, 
          'equals to high school' : 1,
          'more than high school but not college' : 0, 
          'equals to college' : 0}
    n = len(mom) 
    
    prop["less than high school"]=np.sum(mom==1)/n
    prop["equals to high school"]=np.sum(mom==2)/n
    prop["more than high school but not college"]=np.sum(mom==3)/n
    prop["equals to college"]=np.sum(mom==4)/n
    return prop
```

</p>
</details>

<hr>

### SECOND PROJECT ( [project_02](https://github.com/greatti/Data_studies/blob/main/project_02.py) )

<details><summary>DESCRIPTION</summary>
<p>
  
this second project is separated into three parts, but we will work with only two variables: CBF_01 and P_NUMFLU
CBF_01 is a variable that define if the children were or not fed with breastmilk, and it assumes 4 values : [1, 2, 77, 99]. (We find this information at page 177 and 110)
      - 1 It is synonymous for answer "yes"
      - 2 It is synonymous for answer "no"
      - 77 It is synonymous for answer "dont know"
      - 99 It is synonymous for answer "refused"
      
P_NUMFLU is a variable that define the number of doses the children took, it goes from 0.0 to 6.0 including NaN

We basically want to do here 3 studies: 

+ First we will see the average of doses taken by the children of ['CBF_01'] == 1 and ['CBF_01'] == 2 groups, to see if there is a lot of discrepancy in doses taken by these two classes;
+ Secondly, we will see the percentage of elements in each ['CBF_01'] group, to see if the number of elements are similar, because sometimes the study can be impaired by having much more elements in one group than the other; 
+ Lastly, we will see the percentage of children fed on breast milk in each classes in ['P_NUMFLU'], that is, for 6.0, 5.0, 0.0 doses. 

#### Conclusions: 

<table>
<tr><th>First study</th><th>Second study</th><th>Third study</th></tr>
<tr><td>

| CBF_01 | average of doses |
| :---: | :---: |
| 1 | 1.8799187420058687 | 
| 2 | 1.5963945918878317 |

</td><td>

| CBF_01 | Percentage |               
| :---: | :---: |
| 1 | 86.68% |
| 2 | 13.02% |
| 77 | 0.27% |
| 99 | 0.019% |

</td><td>
  
| P_NUMFLU| ['CBF_01']==1 |               
| :---: | :---: |
| 6.0 | 100% |
| 5.0 | 94.28% |
| 0.0 | 83.74% |

</td></tr> </table>

So what can we conclude? Children that have been fed with breastmilk take more doses of flu, in average, when compared to those that have not been fed with breastmilk, but it is kinda similar, that indicates that maybe the number of elements in ['CBF_01'] could be similar too? So we will confirm this by the second study.
The second study proves the opposite, we have MUCH more children fed with breastmilk than all the other options, so that make me think, maybe if we had 25% of children for each class, the average could be different? I think so. 
To confirm that the number of elements influences in average, we do the third study and see that we really have much more children fed with breastmilk in all classes, for both 5 doses and 0 doses

This codes i dont recommend reading before seeing the full project_02, because it is not explicative, is just the pure study code.

```python
def First_project(): 
    import pandas as pd
    import numpy as np 
    df = pd.read_csv('NISPUF17.csv')
    keepcolumns = ['CBF_01', 'P_NUMFLU']
    dfflu = df[keepcolumns]
    dfflu_yes = dfflu[dfflu['CBF_01'] == 1].dropna()
    dfflu_no = dfflu[dfflu['CBF_01'] == 2].dropna()
    y = len(dfflu_yes)
    n = len(dfflu_no)
    y_av = np.sum(dfflu_yes['P_NUMFLU'])/y
    n_av = np.sum(dfflu_no['P_NUMFLU'])/n
    return(y_av, n_av)

def Second_project(): 
    import pandas as pd 
    #import numpy as np 
    df = pd.read_csv('NISPUF17.csv')
    keepcolumns = ['CBF_01', 'P_NUMFLU']
    dfflu = df[keepcolumns]
    
    dfflu_yes = dfflu[dfflu['CBF_01'] == 1].dropna()
    dfflu_no = dfflu[dfflu['CBF_01'] == 2].dropna()
    dfflu_dontknow = dfflu[dfflu['CBF_01'] == 77].dropna()
    dfflu_refuse = dfflu[dfflu['CBF_01'] == 99].dropna()
    y = len(dfflu_yes)
    n = len(dfflu_no)
    dn = len(dfflu_dontknow)
    r = len(dfflu_refuse)
    t = (y + n + dn + r)
    
    yes = (y / t)*100
    no = (n / t)*100
    dontknow = (dn / t)*100
    refused = (r / t)*100
    
    return(yes,no,dontknow,refused)

def Third_project(): 
    #import numpy as np
    import pandas as pd
    
    df = pd.read_csv('NISPUF17.csv')
    keepcolumns = ['CBF_01', 'P_NUMFLU']
    dfflu = df[keepcolumns]

    dmin = min(dfflu['P_NUMFLU'].dropna().unique())
    #dmax = max(dfflu['P_NUMFLU'].dropna().unique())

    #dfflu_doses_max = dfflu[dfflu['P_NUMFLU'] == dmax].dropna()
    dfflu_doses_5 = dfflu[dfflu['P_NUMFLU'] == 5.0].dropna()
    dfflu_doses_min = dfflu[dfflu['P_NUMFLU'] == dmin].dropna()
    
    t5 = len(dfflu_doses_5)
    tmin = len(dfflu_doses_min)
    #tmax = len(dfflu_doses_max)
    
    dfflu_doses_5_1 = dfflu_doses_5[dfflu_doses_5['CBF_01'] == 1]
    dfflu_doses_min_1 = dfflu_doses_min[dfflu_doses_min['CBF_01'] == 1] 
    
    t51 = len(dfflu_doses_5_1)
    tmin1 = len(dfflu_doses_min_1)

    yes_5 = (t51 / t5)*100
    yes_min = (tmin1 / tmin)*100
    
    return(yes_5, yes_min)
```

</p>
</details>

<hr>

### THIRD PROJECT ( [project_03](https://github.com/greatti/Data_studies/blob/main/project_03.py) )

<details><summary>DESCRIPTION</summary>
<p>

This third project is something big, we will have to filter NISPUF17.csv a lot of times, we want to study basically 3 variables: 

['SEX'] that indicates the sex of the child: Male or Female (1 and 2)
['HAD_CPOX'] that indicates if the child had cpox : Yes, No, Dont know, refused or missing (1, 2, 77, 99 and NaN)
['P_NUMVRC'] that indicates the number of varicella doses 

Buy why? We want to see if the the vaccine is effective in male and female children
But how? 

        - First, we get NISPUF17 and filter it to just this three variables;
        - Then, we filter the resulting dataframe to ['HAD_CPOX'] == 1 , that is, only to who had cpox;
        - Then, we filter this resulting dataframe to ['P_NUMVRC'] greater than 1;
        - Last, we filter again separating by sex.

After all that we have this groups: 

        - had cpox, at least one dose, male
        - had cpox, at least one dose, female
        - had cpox, no doses, male
        - had cpox, no doses, female
        - hadnt cpox, at least one dose, male
        - hadnt cpox, at least one dose, female
        - hadnt cpox, no doses, male
        - hadnt cpox, no doses, female
       
And now we count the number of elements of each group to calculate the percentages, we stay with: 
>OBSERVATIONS: 
>> Had_Took: Had cpox and took at least one dose
>> Had_Didnttook: Had cpox and hasnt took any dose
>> Hadnt_Took: Did not contract cpox but took at least one dose
>> Hadnt_Didnttook: Did not contract cpox and hasnt took any dose

<table>
  <tr><th>Had_Took</th><th>Had_Didnttook</th><th>Hadnt_Took</th><th>Hadnt_Didnttook</th></tr>
<tr><td>

| Sex | Percentage |
| :---: | :---: |
| 1 | 70.1% | 
| 2 | 69.7% |

</td><td>

| Sex | Percentage |               
| :---: | :---: |
| 1 | 29.8% |
| 2 | 30.2% |

</td><td>
  
| Sex | Percentage |              
| :---: | :---: |
| 1 | 91.2% |
| 2 | 91.7% |

</td><td>
  
| Sex | Percentage |              
| :---: | :---: |
| 1 | 8.71% |
| 2 | 8.25% |

</td></tr> </table>

That all means: 

              - 70% of mans that had cpox were vaccinated, and 69% of woman that had cpox were vaccinated
              - 29% of mans that had cpox werent vaccinated , and 30% of womand that had cpox werent vaccinated
What all of that means? The vaccine isnt effective? Not necessarily, the percentages are confusing and contradictory 
because we are not seeing all the elements together, so lets put all the percentages with all the elements in a pie
chart

![PieChart](https://github.com/greatti/Data_studies/blob/main/PieChart(p3).png)

And this is what we get, so now we can conclude that the vaccine is really effective both in male and female
We see that even that the percentages were big, the number of elements were not, so the number of people who
hadnt cpox but took the vaccine is WAY too big than of those who had cpoxand took the vaccine, but the percentages
are equal

<hr>

As i said i all of the previous projects, i dont recommend you to read this code bellow, because it is not explicative, it is just the pure code:

```python

def cpox_project(): 
    import pandas as pd
    import numpy as np 
    df = pd.read_csv('NISPUF17.csv')
    keepcolumns = ['SEX', 'P_NUMVRC', 'HAD_CPOX']
    df = df[keepcolumns]
    
    df_yes = df[df['HAD_CPOX'] == 1].dropna()
    df_no = df[df['HAD_CPOX'] == 2].dropna()
    
    df_yes_one = df_yes[df_yes['P_NUMVRC'] > 0.0].dropna()
    df_yes_none = df_yes[df_yes['P_NUMVRC'] == 0.0].dropna()

    df_no_one = df_no[df_no['P_NUMVRC'] > 0.0].dropna()
    df_no_none = df_no[df_no['P_NUMVRC'] == 0.0].dropna()
    
    df_yes_one_m = df_yes_one[df_yes_one['SEX'] == 1].dropna() 
    df_yes_one_f = df_yes_one[df_yes_one['SEX'] == 2].dropna() 

    df_yes_none_m = df_yes_none[df_yes_none['SEX'] == 1].dropna() 
    df_yes_none_f = df_yes_none[df_yes_none['SEX'] == 2].dropna() 

    df_no_one_m = df_no_one[df_no_one['SEX'] == 1].dropna() 
    df_no_one_f = df_no_one[df_no_one['SEX'] == 2].dropna() 

    df_no_none_m = df_no_none[df_no_none['SEX'] == 1].dropna() 
    df_no_none_f = df_no_none[df_no_none['SEX'] == 2].dropna() 
    
    t1 = len(df_yes_one_m)
    t2 = len(df_yes_one_f)
    t3 = len(df_yes_none_m)
    t4 = len(df_yes_none_f)
    t5 = len(df_no_one_m)
    t6 = len(df_no_one_f)
    t7 = len(df_no_none_m)
    t8 = len(df_no_none_f)
    t = (t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8)
    
    had_took={"male":0,
        "female":0} 
    had_didnttook={"male":0,
        "female":0} 

    hadnt_took={"male":0,
        "female":0} 
    hadnt_didnttook={"male":0,
        "female":0} 

    had_took['male']= t1/(t1 + t3)
    had_took['female']= t2 / (t2 + t4) 

    had_didnttook['male'] = t3/(t1 + t3)
    had_didnttook['female'] = t4/(t2 + t4)
    
    hadnt_took['male'] = t5/(t5 + t7)
    hadnt_took['female'] = t6/(t6 + t8)

    hadnt_didnttook['male'] = t7/(t5 + t7)
    hadnt_didnttook['female'] = t8/(t6 + t8)
    
    dfpie = pd.DataFrame({'elements': [t1, t2, t3, t4, t5, t6, t7, t8]},
                  index=['yes_one_m', 'yes_one,f', 'yes_none_m',
                         'yes_none_f', 'no_one_m', 'no_one_f',
                         'no_none_m', 'no_none_f' ])

    plot = dfpie.plot.pie(y='elements', figsize = (8,8))
    
    return(had_took, had_didnttook, hadnt_took, hadnt_didnttook)
    return(plot)
```

</p>
</details>

<hr>
