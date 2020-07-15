import matplotlib.pyplot as plt
import numpy as np




viewslots = np.arange(1000, 10000, step=1000)
print(viewslots)

youtubeviews = np.random.randint(1000, 10000, size=(30,))
print(youtubeviews)

plt.hist(youtubeviews, viewslots, label="View Distribution")

plt.xlabel("Day")
plt.ylabel("Views")

#print(plt.xlim(1,6))
#print(plt.ylim(1000,5000))

plt.legend(loc="best")
plt.grid(color='y', linestyle=':')

plt.title("Channel Views Distribution In Month")

plt.savefig("Channel_views_Histogram.png", dpi=300)

plt.show()