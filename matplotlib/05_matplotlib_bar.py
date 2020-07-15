import matplotlib.pyplot as plt
import numpy as np


day = np.arange(1,31)
print(day)

youtubeviews = np.random.randint(1000, 10000, size=(30,))
print(youtubeviews)

twitterviews = np.random.randint(1000, 10000, size=(30,))
print(twitterviews)

instaviews = np.random.randint(1000, 10000, size=(30,))
print(instaviews)

plt.bar([d+0.2 for d in day], youtubeviews, width=0.4, label="Youtube views", color='r')
plt.bar([d-0.2 for d in day], twitterviews, width=0.4, label="Twitter views", color='g')

plt.xlabel("Day")
plt.ylabel("Views")

#print(plt.xlim(1,6))
#print(plt.ylim(1000,5000))

plt.legend(loc="best")
plt.grid(color='y', linestyle=':')

plt.title("Channel Views In Week")

plt.savefig("Channel_views_Bar.png", dpi=300)

plt.show()