import pandas as pd

#print(help(pd))
#create dataframe from csv file
df = pd.read_excel('toc.xlsx')
print(type(df))
print(df)
print(df.columns)
newdf = df.fillna("ok")
print(newdf)

newdf = df[["Unnamed: 0", 'Content Covered', 'Duration (In hrs.)' ]].fillna("")
print(newdf)