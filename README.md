# An introduction to Pandas library (Python) -- with projects!! 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

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
+ project_01.py **the first project 

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
