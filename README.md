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
