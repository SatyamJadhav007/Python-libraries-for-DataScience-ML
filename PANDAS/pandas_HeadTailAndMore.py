""" 
    topics-6
    df.head(val) -> return rows from the beginning of the dataframe(default:5,"val"->int)
    df.tail(val) -> return rows from the end of the dataframe(default: 5,"val"->int) 
    df.info() ->    returns no.of rows,columns,datatype,non-null no. and memory usage 
    df.describe() ->returns count(),min(),max(),mean(),std(),var(),25%,50%,75% 
    df["column_name"] -> used to extract a series or subset of the dataframe 
    df[df["column_name"]...{conditions}] -> used to filter "custom" data from the dataframe 
"""

import pandas as pd 

df=pd.read_csv("large_ecommerce_sales_data.csv") 

# head() -> return first 5 rows of the datafrome(default) 
print("Data from  head() function")
print(df.head(10))

# tail() -> return rows from the end of the dataframe(default: 5) 
print("Data from tail() function")
print(df.tail(10)) 

""" 
info()  
-> number of rows and columns 
-> column name(with data type,Non-Null-count) 
-> All the datatypes 
-> memory usage 
""" 

print("Data from info() function")
print(df.info()) 

data={
    "Name":["Aizen","Light","Johan","Lelouche","Ayanokoji","Urahara"], 
    "Age":[24,25,19,20,18,34], 
    "City":["karakura town","tokyo","shinjuku","tokyo","shibuya","tokyo"], 
    "Aura":[99,98,99,97,93,96]
}

df_data=pd.DataFrame(data) 
print("Sample dataframe") 
print(df_data) 
print("Descriptive stats") 
""" 
    .describe() -> return the following data about the dataframe 
    -> count,mean,std,min,25%,50%,75%,max for the numerical columns  
    -> What are 25%,50%,75%?? 
    -> ex. ->[18,19,20,24,25,34,36,37] then 25% is [18,19],50% is [20,24], 75% is [25,34] and so on 
    -> They are like a minimum threshold for "that" percentage of data for "that" particular dataset! 
"""
print(df_data.describe()) 
# .shape -> return the number of rows and columns in the datasets 
# .columns -> returns the number of columns in the dataset 
print("Shape",df_data.shape) 
print("Column",df_data.columns) 

# select specific column -> square brackets ,boolean indexing 
""" 
   column=df["col1","col2",...] <-- series!!!(1D array)
"""
columns=df_data[["Name","Aura"]] 
""" 
   boolean indexing syntax
   df[df["column name"] condition] 
   it is like , SELECT * FROM table WHERE condition 
"""
print("Data of seleted columns:") 
print(columns)
filtered_rows=df_data[(df_data["Age"]>21) & (df_data["City"]=="tokyo")]

print("Filtered rows :") 
print(filtered_rows)