import matplotlib.pyplot as plt
import numpy as np


day = np.arange(1,8)
print(day)

youtubeviews = np.random.randint(1000, 10000, size=(7,))
print(youtubeviews)

twitterviews = np.random.randint(1000, 10000, size=(7,))
print(twitterviews)

instaviews = np.random.randint(1000, 10000, size=(7,))
print(instaviews)



plt.plot(day, youtubeviews, label="Youtube Views", color='r', marker="D", markerfacecolor='b', linewidth=1)
plt.plot(day, twitterviews, label="Twitter Views", color='b', marker="s", markerfacecolor='r', linewidth=1)
plt.plot(day, instaviews, label="Insta Views", color='g', marker="X", markerfacecolor='y', linewidth=1)

plt.xlabel("Day")
plt.ylabel("Views")

#print(plt.xlim(1,6))
#print(plt.ylim(1000,5000))

plt.legend(loc="best")
plt.grid(color='y', linestyle='-')

plt.title("Channel Views In Week")

plt.savefig("Channel_views.png", dpi=300)

plt.show()