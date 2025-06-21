""" 
   topics- 2
   reading data from csv/exce/json files -> pd.read_json(filePath) 
   writing data to csv/excel/json files -> df.to_json(fileName,index=False/True) 
"""


#understanding data  
import pandas as pd 
#reading data from csv file as a dataframe(2-D array) 
# utf-8 , latin-1 <-- encoding standards  

#WAYS TO READ FILES IN PANDAS
#df=pd.read_csv("ecommerce_sales_data.csv") 
#df=pd.read_excel("ecommerce_sales_data.xlsx") 
df=pd.read_json("ecommerce_sales_data.json")
print(df) 

# gcsfs library=> used to read data from cloud storage 

# converting dataframe to csv/json/excel file 
#dataframe.to_csv(name,index=False,More) index=False ->remove the default indentification of rows
data={
    "Name":["Aizen","Light","Johan"], 
    "Age":[24,25,19], 
    "City":["karakura town","tokyo","shinjuku"]
}

df_data=pd.DataFrame(data) 
#print(df_data) 
#df_data.to_csv("output.csv",index=False) 

#dataframe.to_excel(name,index=False,More)

df_data.to_excel("output.xlsx",index=False) 

#dataframe.to_json(name,index=False,More)
df_data.to_json("output.json",index=False)