import matplotlib.pyplot as plt
import numpy as np

# first plot
a= np.array([1,2,3,4])
b = np.array([1,2,3,4])

plt.subplot(1,2,1)
plt.plot(a,b,'o-r')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Array chart")

# second plot
a1 = np.array([1,2,3])
b1 = np.array([1,2,3])

plt.subplot(1,2,2)
plt.plot(a1,b1,'o-r')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Array 2 chart")
plt.show()


