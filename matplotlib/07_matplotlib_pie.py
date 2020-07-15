import matplotlib.pyplot as plt
import numpy as np

social = ['youtube', 'twitter', 'facebook', 'instagram', 'linkedin', 'flickr', 'telegram', 'patreon']
followers = np.random.randint(1000,5000, size=(8,))
print(social)
print(followers)

explodevalue = [0,0,0.2,0,0,0,0, 0]

plt.pie(followers, labels=social, explode=explodevalue, wedgeprops={'width':0.5}, autopct='%1.1f%%')

plt.show()