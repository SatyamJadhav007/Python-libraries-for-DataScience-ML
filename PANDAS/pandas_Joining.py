""" 
    topics-2
    Joining 2 dataframes:
    pd.merge(df1,df2,on="column_name",how="inner/left/right/outer/cross")  
   ->inner => common values 
   -> outer => all values 
   -> cross => cartesian product of all values 
   -> left => left dataframe values (all)
   -> right => right dataframe values (all)

   concatenating dataframe values (vertical/horizontal)
   pd.concate(df1,df2,axis=0/1,ignore_index=True/False)
   axis-> 0 => row-wise 
   1=> column-wise 
"""

import pandas as pd 
#pd.set_option('display.max_columns', None)
customers_2024 = [
    {"CustomerID": 1, "Name": "Alice", "Email": "alice@example.com", "Country": "India", "SignupDate": "2024-01-10", "TotalSpent": 120.50},
    {"CustomerID": 2, "Name": "Bob", "Email": "bob@example.com", "Country": "USA", "SignupDate": "2024-02-12", "TotalSpent": 250.00},
    {"CustomerID": 3, "Name": "Charlie", "Email": "charlie@example.com", "Country": "UK", "SignupDate": "2024-03-15", "TotalSpent": 175.20},
    {"CustomerID": 4, "Name": "Diana", "Email": "diana@example.com", "Country": "Canada", "SignupDate": "2024-04-01", "TotalSpent": 90.30},
    {"CustomerID": 5, "Name": "Ethan", "Email": "ethan@example.com", "Country": "India", "SignupDate": "2024-05-06", "TotalSpent": 300.75},
    {"CustomerID": 6, "Name": "Fiona", "Email": "fiona@example.com", "Country": "USA", "SignupDate": "2024-06-10", "TotalSpent": 145.00},
    {"CustomerID": 7, "Name": "George", "Email": "george@example.com", "Country": "Germany", "SignupDate": "2024-07-15", "TotalSpent": 210.00},
    {"CustomerID": 8, "Name": "Hannah", "Email": "hannah@example.com", "Country": "France", "SignupDate": "2024-08-22", "TotalSpent": 400.00},
    {"CustomerID": 9, "Name": "Ian", "Email": "ian@example.com", "Country": "Australia", "SignupDate": "2024-09-30", "TotalSpent": 50.00},
    {"CustomerID": 10, "Name": "Jenny", "Email": "jenny@example.com", "Country": "USA", "SignupDate": "2024-10-18", "TotalSpent": 600.00},
    {"CustomerID": 11, "Name": "Karl", "Email": "karl@example.com", "Country": "Germany", "SignupDate": "2024-11-12", "TotalSpent": 270.25},
    {"CustomerID": 12, "Name": "Laura", "Email": "laura@example.com", "Country": "India", "SignupDate": "2024-11-30", "TotalSpent": 325.10},
    {"CustomerID": 13, "Name": "Mike", "Email": "mike@example.com", "Country": "Brazil", "SignupDate": "2024-12-05", "TotalSpent": 85.00},
    {"CustomerID": 14, "Name": "Nina", "Email": "nina@example.com", "Country": "UK", "SignupDate": "2024-12-20", "TotalSpent": 500.00},
    {"CustomerID": 15, "Name": "Oscar", "Email": "oscar@example.com", "Country": "Mexico", "SignupDate": "2024-12-28", "TotalSpent": 190.90}
]
customers_2025 = [
    {"CustomerID": 3, "Name": "Charlie", "Email": "charlie@example.com", "Country": "UK", "SignupDate": "2025-01-05", "TotalSpent": 200.00},
    {"CustomerID": 4, "Name": "Diana", "Email": "diana@example.com", "Country": "Canada", "SignupDate": "2025-01-18", "TotalSpent": 130.00},
    {"CustomerID": 6, "Name": "Fiona", "Email": "fiona@example.com", "Country": "USA", "SignupDate": "2025-02-14", "TotalSpent": 220.00},
    {"CustomerID": 10, "Name": "Jenny", "Email": "jenny@example.com", "Country": "USA", "SignupDate": "2025-03-21", "TotalSpent": 450.00},
    {"CustomerID": 13, "Name": "Mike", "Email": "mike@example.com", "Country": "Brazil", "SignupDate": "2025-04-12", "TotalSpent": 95.00},
    {"CustomerID": 16, "Name": "Paul", "Email": "paul@example.com", "Country": "India", "SignupDate": "2025-05-03", "TotalSpent": 170.00},
    {"CustomerID": 17, "Name": "Queenie", "Email": "queenie@example.com", "Country": "USA", "SignupDate": "2025-05-25", "TotalSpent": 310.00},
    {"CustomerID": 18, "Name": "Ron", "Email": "ron@example.com", "Country": "UK", "SignupDate": "2025-06-10", "TotalSpent": 290.00},
    {"CustomerID": 19, "Name": "Sara", "Email": "sara@example.com", "Country": "India", "SignupDate": "2025-07-19", "TotalSpent": 410.00},
    {"CustomerID": 20, "Name": "Tom", "Email": "tom@example.com", "Country": "Germany", "SignupDate": "2025-08-20", "TotalSpent": 360.00},
    {"CustomerID": 21, "Name": "Uma", "Email": "uma@example.com", "Country": "France", "SignupDate": "2025-09-10", "TotalSpent": 240.00},
    {"CustomerID": 22, "Name": "Victor", "Email": "victor@example.com", "Country": "Canada", "SignupDate": "2025-10-01", "TotalSpent": 180.00},
    {"CustomerID": 23, "Name": "Wendy", "Email": "wendy@example.com", "Country": "Australia", "SignupDate": "2025-10-22", "TotalSpent": 265.00},
    {"CustomerID": 24, "Name": "Xavier", "Email": "xavier@example.com", "Country": "India", "SignupDate": "2025-11-15", "TotalSpent": 390.00},
    {"CustomerID": 25, "Name": "Yara", "Email": "yara@example.com", "Country": "Mexico", "SignupDate": "2025-12-03", "TotalSpent": 215.00}
]

df_2024=pd.DataFrame(customers_2024) 
df_2025=pd.DataFrame(customers_2025) 
#print(df_2025.info())
#print(df_2025.describe())
""" 
   joining 2 dataframes 
   pd.merge(df1,df2,on="column_name",how="inner/left/right/outer/cross")  
   ->inner => common values 
   -> outer => all values 
   -> cross => cartesian product of all values 
   -> left => left dataframe values (all)
   -> right => right dataframe values (all)
"""
df_merged=pd.merge(df_2024,df_2025,on="CustomerID",how="inner")

print("the merged data is:")
print(df_merged) 

""" 
  concatenating dataframe values (vertical/horizontal)
  pd.concate(df1,df2,axis=0/1,ignore_index=True)
  axis-> 0 => row-wise 
  1=> column-wise 
"""

df_concat=pd.concat([df_2024,df_2025],axis=0,ignore_index=True)
print("the concatenated data is:")
print(df_concat)