import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,10)
print(x)
y = np.random.randint(50, 100, size=(9,))
print(y)

plt.plot(x, y)
plt.show()