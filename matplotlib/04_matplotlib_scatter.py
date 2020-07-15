import matplotlib.pyplot as plt
import numpy as np


day = np.arange(1,366)
print(day)

youtubeviews = np.random.randint(1000, 10000, size=(365,))
print(youtubeviews)

twitterviews = np.random.randint(1000, 10000, size=(365,))
print(twitterviews)

instaviews = np.random.randint(1000, 10000, size=(365,))
print(instaviews)

plt.scatter(day, youtubeviews, label="Youtube Views", color='r', marker="D")
#plt.scatter(day, twitterviews, label="Twitter Views", color='b', marker="s")
#plt.scatter(day, instaviews, label="Insta Views", color='g', marker="X")

plt.xlabel("Day")
plt.ylabel("Views")

#print(plt.xlim(1,6))
#print(plt.ylim(1000,5000))

plt.legend(loc="best")
plt.grid(color='y', linestyle=':')

plt.title("Channel Views In Week")

plt.savefig("Channel_views_Scatter.png", dpi=300)

plt.show()