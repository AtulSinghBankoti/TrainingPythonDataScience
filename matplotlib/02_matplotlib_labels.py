import matplotlib.pyplot as plt
import numpy as np


day = np.arange(1,8)
print(day)
views = np.random.randint(1000, 10000, size=(7,))
print(views)

plt.plot(day, views, label="Channel Views", color='r', marker="D", markerfacecolor='b', linewidth=1)

plt.xlabel("Day")
plt.ylabel("Views")

plt.legend(loc="best")

plt.title("Channel Views In Week")
plt.show()