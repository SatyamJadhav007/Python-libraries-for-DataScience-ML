""" 
   topics- 3
   df.sort_values(by="column_name",ascending=True/False,inplace-True/False) -> used to sort the dataframe by "that" column/columns 
   df["column_name"].method() -> used to perform aggregation on a single series/subset of the dataframe
   -> method => mean(),std(),var(),sum(),count(),min(),max(),etc... 
   df.groupby("column_name")["column_name_for_aggregation"].method() -> used to get detailed insights from a subset of the dataframe 
"""

import pandas as pd 
pd.set_option('display.max_columns', None)
# sorting data frame 
""" 
   df.sort_values(by="Column_name",{ascending/descending}True/False,inplace=True/False) 
   -> True ->Ascending order sorting 
   -> False -> Descending order sorting  
"""
employees = [
    {
        "ID": 101,
        "Name": "Alice Johnson",
        "Age": 29,
        "Department": "HR",
        "Salary": 55000,
        "FullTime": True
    },
    {
        "ID": 102,
        "Name": "Bob Smith",
        "Age": 35,
        "Department": "Engineering",
        "Salary": 72000,
        "FullTime": True
    },
    {
        "ID": 103,
        "Name": "Charlie Lee",
        "Age": 24,
        "Department": "Engineering",
        "Salary": 88000,
        "FullTime": False
    },
    {
        "ID": 104,
        "Name": "Diana Prince",
        "Age": 41,
        "Department": "Sales",
        "Salary": 61000,
        "FullTime": True
    },
    {
        "ID": 105,
        "Name": "Ethan Hunt",
        "Age": 31,
        "Department": "Sales",
        "Salary": 67000,
        "FullTime": False
    },
    {
        "ID": 106,
        "Name": "Peter Parker",
        "Age": 36,
        "Department": "Sales",
        "Salary": 70000,
        "FullTime": True
    },
]

df=pd.DataFrame(employees) 
df.sort_values(by="Age",ascending=False,inplace=True)
print("Sorted in descending order by age...")
print(df) 
# pass list of column names to sort it by "them"
df.sort_values(by=["Age","Salary"],ascending=[True,True],inplace=True) 
print("Sorted by age and salary in descending order...") 
print(df)

""" 
   df["column_name"].method()
   -> method => mean(),std(),var(),sum(),count(),min(),max(),etc... 
"""

avg_salary=df["Salary"].mean() 
print("the average salary is:",avg_salary)

""" 
   GROUPOING SINGLE COLUMN
   df.groupby("column_name")["column_name_for_aggregation"].method() 
   method -> mean(),std(),count(),min(),max(),
   GROUPING MULTIPLE COLUMNS
   df.groupby(["column_1","column_2"])["column_name_for_aggregation"].method()
"""

avg_salary_by_FullTime=df.groupby("FullTime")["Salary"].mean() 
print(avg_salary_by_FullTime)

#grouping by multiple columns
avg_salary_by_FullTime_and_Department=df.groupby(["FullTime","Department"])["Salary"].mean() 
print(avg_salary_by_FullTime_and_Department)