import pandas as pd

df=pd.read_csv("Superstore_Dataset.csv",encoding='latin1')

#droping null value
df.dropna(inplace=True)

df['Order Date']=pd.to_datetime(df['Order Date'])
df['Ship Date']=pd.to_datetime(df['Ship Date'])

df["MonthYear"]=df["Order Date"].dt.to_period('M')

df.to_csv("Superstore_Cleaned_Dataset.csv")
print("Cleaned file created!")