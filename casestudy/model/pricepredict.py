import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data
df1 = pd.read_csv("Bengaluru_House_Data.csv")
print(df1.shape)

print(df1)

#investigate area type
#get the count of all area types

print(df1.groupby('area_type')['area_type'].agg('count'))
#looks like area type is not necessary
# drop are un-necessary columns!

df2 = df1.drop(['area_type','society','balcony', 'availability'], axis='columns')

print(df2.head())

#check for null values in all rows
print(df2.isnull().sum())

#drop all rows with null values
df3 = df2.dropna()
#check for null values in all rows
print(df3.isnull().sum())

print(df3.shape)
print(df3.head(20))

#get all unique values in size column
print(df3['size'].unique())
print(df3['size'].unique().size)

#create new column bhk which will contain numberic value from 4 BHK or 4 Bedroom
# or 6 BHK or 6 Bedroom
df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))

print(df3.head())


#get all unique values in size column
print(df3['bhk'].unique())
print(df3['bhk'].unique().size)

#get those rows with bhk > 15
print(df3[df3.bhk > 15])

#get all unique total_sqft
print(df3.total_sqft.unique())
print(df3.total_sqft.unique().size)

#some total_sqft are in range. 

#check all total_sqft values which are pure numbers!

def check_if_float(x):
    try:
        float(x)
    except:
        return False
    return True      

print(df3[df3['total_sqft'].apply(check_if_float)].head(20)      )
print(df3[df3['total_sqft'].apply(check_if_float)].size  )  

#check all total_sqft values which are non-numbers!

print(df3[~df3['total_sqft'].apply(check_if_float)].head(20)  )    
print(df3[~df3['total_sqft'].apply(check_if_float)].size  )  

#convert all total_sqft (in range) to single float values (avg)
def convert_sqft_range_to_float(x):
    temp = x.split('-')
    if(len(temp) == 2):
        return (float(temp[0])+float(temp[1]))/2
    try:
        return float(x)    
    except:
        return None    

df4 = df3
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_range_to_float) 

print(df4.head(40))

print(df4.loc[137])
print(df4.loc[648])

#ADD NEW COLUMN FOR price_per_sqft
df5 = df4.copy()
df5['price_per_sqft']=df5['price']*100000/df5['total_sqft']
print(df5.head(40))
print(df5.shape)

#get unique values from location column
print(df5.location.unique().size)

df5.location = df5.location.apply(lambda x: x.strip())

#group by location 

print(df5.groupby('location')['location'].agg('count'))

#ascending 
print(df5.groupby('location')['location'].agg('count').sort_values(ascending=False))

#get all locations with less than 10 homes/rows

filter = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)
print(filter)

print(len(filter[filter<=10]))
all_locations_with_houses_less_than10 = filter[filter<=10]
print(all_locations_with_houses_less_than10)
#rename all location with houses less than 10 to others

df5.location = df5.location.apply(lambda x: 'other' if x in all_locations_with_houses_less_than10 else x)

print(df5.location.unique())
print(df5.location.unique().size)
print(df5.head())


#detecting outliers and removing them!
print(df5.head(30))

#get the dataframe where sqft for each room is less than 300
print(df5[df5.total_sqft/df5.bhk<300].head())
print(df5[df5.total_sqft/df5.bhk<300].size)

#get the new dataframe where sqft of each room is more than 300
df6 = df5[~(df5.total_sqft/df5.bhk<300)]
print(df6.head)
print(df6.size)

#get more information from price_per_sqft
print(df6.price_per_sqft.describe())

#define the function to remove extremes in price_per_sqft

def remove_extremes_ppsft(dataframe):
    df_return = pd.DataFrame()
    for key, df_temp in dataframe.groupby('location'):
        mean_temp = np.mean(df_temp.price_per_sqft)
        std_temp = np. std(df_temp.price_per_sqft)
        filtered_df = df_temp[(df_temp.price_per_sqft > (mean_temp-std_temp)) & (df_temp.price_per_sqft <= (mean_temp + std_temp))]
        df_return = pd.concat([df_return, filtered_df], ignore_index=True)
    return df_return
        

df7 = remove_extremes_ppsft(df6)
print(df7.shape)
print(df7.size)


#plot the scatter chart for some area -> Doddathoguru to see distribution of prices
# for 2 bhk and 3 bhk

'''
def plot_scatter_for_location(df, location):
    bhk2 = df[(df.location == location) & (df.bhk == 2)]
    bhk3 = df[(df.location == location) & (df.bhk == 3)]
    plt.scatter(bhk2.total_sqft, bhk2.price, color="blue", label="2 BHK", s=50)
    plt.scatter(bhk3.total_sqft, bhk3.price, color="blue", label="3 BHK", s=50, marker="+")
    plt.xlabel("Total Sq Ft Area")
    plt.ylabel("price")
    plt.title(location)
    plt.legend()
    plt.show()



plot_scatter_for_location(df7, "Electronic City Phase II")
'''

#get all unique bathrooms
print(df7.bath.unique())

#plot histogram to get how many bathrooms are in how many homes.

'''
plt.hist(df7.bath, rwidth=0.4)
plt.xlabel("Number of bathrooms")
plt.ylabel("Count")
plt.show()

'''

print(df7[df7.bath>10])

df8 = df7[df7.bath<df7.bhk+2]
print(df8.shape)
#df8.to_csv("df8.csv", index=False)
print(df8.head(20))

df10 = df8.drop(['size', 'price_per_sqft'], axis='columns')
print(df10.head())

#use hot encoding for location feature to convert its values to numeric
temp = pd.get_dummies(df10.location)
print(temp.head(50))
print(temp.tail(50))
#combine temp and df10
df11 = pd.concat([df10, temp], axis='columns')
print(df11.shape)
print(df11.head(20))

df12 = df11.drop('location', axis='columns')
print(df12.shape)
print(df12.head(20))

#build a model
# x -> independent values
# y-> will depend on x
x = df12.drop(['price'], axis='columns')
print(x.head(4))
y = df12.price
print(y.head(4))

#split the data to use for training and (testing) success-rate of training
 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y , test_size=0.2, random_state=10)

from sklearn.linear_model import LinearRegression

linearregression = LinearRegression()
p = linearregression.fit(x_train, y_train) #80%
s = linearregression.score(x_test, y_test)  #20%

print(p)
print(s)

# use k fold cross validation to get accuracy of linearregression model

from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

crossvalidation = ShuffleSplit(n_splits= 4, test_size=0.2, random_state = 0)
score = cross_val_score(LinearRegression(), x, y, cv = crossvalidation)
print(score)

#use GridSearchCV to estimate best algorithm

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor

def find_best_algo_using_gridsearchcv(x, y):
    #configuration object for the logic
    configuration = {
        'linear_regression':{
            'model':LinearRegression(),
            'parameters':{
                'normalize':[True, False]
            }
        },
        'lasso':{
            'model':Lasso(),
            'parameters':{
                'alpha':[1, 2],
                'selection':['random','cyclic']
            }
        },
        'decision_tree':{
            'model':DecisionTreeRegressor(),
            'parameters':{
                'criterion':['mse', 'friedman_mse'],
                'splitter':['best', 'random']
            }
        }
    }

    scores = []
    crossvalidation = ShuffleSplit(n_splits=20, test_size=0.2, random_state=0)
    #run the loop on configuration dictionary to get score of each algorithm
    for algo_name, config in configuration.items():
        gs = GridSearchCV(config['model'], config['parameters'], cv=crossvalidation, return_train_score=False)
        gs.fit(x, y)
        scores.append({
            'model':algo_name,
            'best_score':gs.best_score_,
            'best_params':gs.best_params_
        })
    return pd.DataFrame(scores)



#print(find_best_algo_using_gridsearchcv(x,y))
#best algo turns out to be -> linear regression

print(x.columns)
print(np.where(x.columns=='1st Block Jayanagar')[0][0])

def predictprice(location, sqft, bath, bhk):
    locationIndex = np.where(x.columns==location)[0]
    params = np.zeros(len(x.columns))
    params[0]=sqft
    params[1]=bath
    params[2]=bhk
    if(locationIndex>=0):
        params[locationIndex]=1
    return linearregression.predict([params])[0]


print(predictprice('1st Block Jayanagar',1000, 2, 2)    )    
print(predictprice('1st Block Jayanagar',1000, 3, 3)    )
print(predictprice('1st Block Jayanagar',1000, 4, 4)    )
print(predictprice('Vittasandra',1000, 2, 2)    )
print(predictprice('Yeshwanthpur',1000, 2, 2)    )
print(predictprice('Whitefield',1000, 2, 2)    )
print(predictprice('Electronic City',1000, 2, 2)    )
print(predictprice('Indira Nagar',1000, 2, 2)    )
print(predictprice('Indira Nagar',1000, 3, 3)    )
print(predictprice('Indira Nagar',1000, 4, 4)    )
print(predictprice('Indira Nagar',1000, 2, 3)    )

import pickle
with open('bengaluru_home_price_model.pickle', 'wb') as f:
    pickle.dump(linearregression, f)    


import json
columns = {
    'locations':[column.lower() for column in x.columns]
}

with open('location.json',"w") as f:
    f.write(json.dumps(columns))
