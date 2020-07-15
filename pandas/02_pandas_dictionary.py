import pandas as pd

#print(help(pd))
#create dataframe from csv file
df = pd.read_csv("basic_weather.csv")
print(type(df))
print(df)

print(df.shape)


#what is index of given df
print(df.index)
print(df.columns)
#set type column as index column
df.set_index(' type', inplace=True)
#what is index of given df
print(df.index)


#get those rows where type is something
print(df.loc[' sunny'])

#reset index
df.reset_index(inplace=True)
print(df.index)


df['newtype']=df[' type'].str.strip()

print(df)

#write updated data back to csv file

df.to_csv("updated_weather.csv")

#drop column
newdf = df.drop(columns=' type')
print(newdf)