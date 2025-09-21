import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(170,10,200)
b = np.random.normal(130,10,200)
c = np.random.normal(100,10,200)


plt.hist([a,b,c],bins=30,label=['a','b','c'],alpha=0.7,edgecolor='black')
plt.xlabel('vibration')
plt.ylabel('frequency')
plt.title('Histogram Graph')
plt.legend()
plt.show()