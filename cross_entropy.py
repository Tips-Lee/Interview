import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 1, 100, endpoint=False)
y = -x * np.log(x)
# print(x)

plt.plot(x, y)
plt.show()