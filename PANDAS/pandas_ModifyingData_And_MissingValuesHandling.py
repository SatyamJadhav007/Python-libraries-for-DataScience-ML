""" 
   topics-9
   df["new_column_name"]= value{here "value" can be a series or a subset of the dataframe} -> used to add a new column (!position_specified)
   df.insert(location,"column_name",value) -> used to add a new column (position_specified) 
   df.loc[row_index,"column_name"]=value -> used to update data in the dataframe (single/trageted) 
   df.drop(columns=["col1","col2",...],inplace=True/False) -> used to remove columns in the dataframe(position_specified) 
   df.isnull() -> return true if there are null values in the dataframe 
   df.isnull().sum() -> tells the count of the null values in the dataframe 
   df.dropna(axis=0/1,inplace=True/False) -> removes rows/columns with null/NaN values values  
   df.fillna(value,inplace=True/False) -> used to fill the missing values in the dataframe 
   df.interpolate(method="linear/...",axis=0/1,inplace=True/False) -> used to fill the missing values with a predicted value
"""

import pandas as pd 
pd.set_option('display.max_columns', None)

data={
    "Name":["Aizen","Light","Johan","Lelouche","Ayanokoji",None], 
    "Age":[24,25,19,20,18,None], 
    "City":["karakura town","tokyo","shinjuku","tokyo","shibuya",None], 
    "Aura":[99,98,99,97,93,None]
} 
df=pd.DataFrame(data) 

"""  
    Adding a column to the dataframe
"""
print("Before adding a column...")
print(df)
# Adding a column 
df["Bonus_Aura"]=df["Aura"]*0.1 
print("After adding a column...")
print(df)

""" 
   insert(location,"name",data) <- to insert into the dataframe
"""
df.insert(0,"Rank",["1st","2nd","3rd","4th","5th","6th"]) 
print("After inserting a column...(custom insert can be used anywhere)")
print(df)

""" 
   updating data in dataFrames
   ->. loc[] => single update ,+-//%= for multiple updates
   -> kitwa record konta "column" madye ahe?? =>tyala update kr dada
   df.loc[row_index,"column_name"] = new_value
""" 
df.loc[2,"Aura"]=100 
print("After updating a column ....") 
print(df)
# updating multiple columns at the same time 

df["Aura"]=df["Aura"]-0.05 
print("After updating rows of a column ...") 
print(df) 


"""  
   Removing columns 
   -> df.drop(columns=["col1","col2",...],inplace=True) 
   -> inplace-True => permanent change on the dataframe Else it creates a copy
   -> the "columns" specified will be deleted 
"""

df.drop(columns=["Rank"],inplace=True)

print("After removing a column ...") 
print(df) 


""" 
    df.isnull() -> return true if the value is null/None 
    df.isnull().sum() -> tells the count of the missing values
"""
print("Are there any null values in the dataframe?")
print(df.isnull()) 
print(df.isnull().sum()) 


""" 
    Handling missing values 
    df.dropna(axis=0/1/None,inplace=True/False)
    -> axis=0 -> drop rows with missing values 
    -> axis=1 -> drop columns with missing values 

    df.fillna(value,inplace=True/False)
    df.interpolate(method,axis=0/1,inplace=True/False)
    -> method-> linear interpolation ,polynomial interpolation and time interpolation 
"""
#Removing rows/column (missing)
#   df.dropna(axis=0,inplace=True) 
#   print("After dropping rows in missing values ...")
#   print(df)

# filling missing values (all)
#   df.fillna(value=0,inplace=True)
#   print("After filling missing values in the dataframe ...") 
#   print(df)

#filling missing values (specific column)
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Name"].fillna("Urahara",inplace=True)
df.fillna({"Aura":df["Aura"].mean(),"Bonus_Aura":df["Bonus_Aura"].mean(),"City":"tokyo"},inplace=True)
print("After filling missing values for a specific column ...") 
print(df)

# Filling missing data using interpolation
data_Linear={
    "Time":[1,2,3,4,5], 
    "Value":[10,None,30,None,50]
}

df_linear=pd.DataFrame(data_Linear) 

print("Before interpolation...") 
print(df) 

print("After interpolation...") 
""" 
   Used in time series data 
   avoid dropping data instead do this ....  
"""
df_linear["Value"]=df_linear["Value"].interpolate(method="linear")
print(df_linear)

