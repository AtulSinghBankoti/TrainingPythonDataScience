from sklearn.feature_extraction.text import CountVectorizer

tweets = []
tweets_labels = []

with open("positivetweets.txt","rb") as f:
    for tweet in f:
        tweets.append(tweet)
        tweets_labels.append('pos')

with open("negativetweets.txt", "rb") as f:
    for tweet in f:
        tweets.append(tweet)
        tweets_labels.append('neg')

#use CountVectorizer to convert tweets to features
#create config
vectorizer = CountVectorizer(
    analyzer='word',
    lowercase='False',
    max_features=80
)       

#supply tweets to vectorizer
features = vectorizer.fit_transform(tweets)
#convert features to array 
features_array = features.toarray();

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(features_array, tweets_labels , test_size=0.2, random_state=10)

#use logisticregression as algorithm
from sklearn.linear_model import LogisticRegression

logisticregression = LogisticRegression()
p = logisticregression.fit(x_train, y_train) #80%
s = logisticregression.score(x_test, y_test)  #20%

print(p)
print(s)

prediction = logisticregression.predict(x_test)

import random

j = random.randint(0, len(x_test)-7)
for i in range(j, j+7):
    print(prediction[0])
    index = features_array.tolist().index(x_test[i].tolist())
    print(tweets[index].strip())


