import matplotlib.pylab as plt
import numpy as np

a = np.array([1,2,6,9,0,4,2])
b = np.array([0,4,1,6,8,2,6])
plt.scatter(a,b)

a1 = np.array([1,9,6,9,10,4,2])
b1 = np.array([10,7,1,6,8,7,9])

# plt.subplot(2,1,2)
plt.scatter(a1,b1)
plt.show()