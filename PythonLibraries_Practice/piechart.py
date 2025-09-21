import matplotlib.pyplot as plt
import numpy as np

a = np.array([34,22,15,29,32])
mylabel = np.array(['a','b','c','d','e'])
myexplode = [0.2,0,0,0,0]

plt.pie(a, labels=mylabel , explode=myexplode  ,shadow=True)
plt.legend(title="labels")
plt.show()