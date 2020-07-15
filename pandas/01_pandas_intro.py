import pandas as pd

#print(help(pd))
#create dataframe from csv file
df = pd.read_csv("weather.csv")
print(type(df))
print(df)

#print statistical summary of dataframe
print(df.describe())

#print first few rows only
print(df.head(20))

#print last few rows
print(df.tail(20))

print('-----------------------------------')
print(df.columns)

#print selective columns
print(df[['date', 'maximum temperature','snow fall']])
print('-----------------------------------')
#get maximum value in maximum temperature column
print(df['maximum temperature'].max())
print(df['maximum temperature'].min())

print('-----------------------------------')

#use filters on dataframe
#print all rows with maximum temperature more than 90
print(df.loc[df['maximum temperature']>90])
print('---------------------------------------')
#get those with T in precipitation
print(df.loc[df['precipitation']=='T'])
