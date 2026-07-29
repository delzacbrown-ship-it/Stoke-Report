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

leads_dict = {'A': 799, 'B': 334, 'C': 333}
Pre_Scaled_Leads = {'A': 332, 'B': 334, 'C': 333}
Pre_Scaled_Opportunaties = {'A': 10, 'B': 8, 'C': 4}
Scaled_Opportunaties = {'A': 29, 'B': 14, 'C': 6}

df_merged = pd.concat([df1,df2,df3])

print(df_merged)

df_summary = df_merged.groupby('Campaign')[['Sent', 'Replied' ]].sum()
df_summary['Leads'] = df_summary.index.map(leads_dict)
df_summary['Pre_Scaled_Leads'] = df_summary.index.map(Pre_Scaled_Leads)
df_summary['Pre_Scaled_Opportunaties'] = df_summary.index.map(Pre_Scaled_Opportunaties)
df_summary['Scaled_Opportunaties'] = df_summary.index.map(Scaled_Opportunaties)

df_summary['Leads_Reply_Rate'] = round(100*df_summary.Replied/df_summary.Leads, 2)
df_summary['Pre_Scaled_Opportunaties_Rate'] = round(100*df_summary.Pre_Scaled_Opportunaties/df_summary.Pre_Scaled_Leads, 2)
df_summary['Scaled_Opportunaties_Rate'] = round(100*df_summary.Scaled_Opportunaties/df_summary.Leads, 2)


print(df_summary)
