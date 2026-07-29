import pandas as pd 

df1 = pd.read_csv('Instantly Analytics - Stoke Campaign 1.csv')
df2 = pd.read_csv('Instantly Analytics - Stoke Campaign 2.csv')
df3 = pd.read_csv('Instantly Analytics - Stoke Campaign 3.csv')

print(df1)

df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()
df3.columns = df3.columns.str.strip()

df1.columns = df1.columns.str.replace(' ', '_')
df2.columns = df2.columns.str.replace(' ', '_')
df3.columns = df3.columns.str.replace(' ', '_')

df1 = df1.drop(columns=['Opened','Unique_Opened','Link_Clicks','Unique_Link_Clicks'])
df2 = df2.drop(columns=['Opened','Unique_Opened','Link_Clicks','Unique_Link_Clicks'])
df3 = df3.drop(columns=['Opened','Unique_Opened','Link_Clicks','Unique_Link_Clicks'])

df1['Campaign'] = 'A'
df2['Campaign'] = 'B'
df3['Campaign'] = 'C'


df_merged = pd.concat([df1,df2,df3])

print(df_merged)