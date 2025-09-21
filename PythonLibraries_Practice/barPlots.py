import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D','E','F','G','H'])
y = np.random.randint(1,8 ,size=8)
plt.subplot(2,1,1)
plt.bar(x,y,height=0.3)
plt.subplot(2,1,2)
plt.barh(x,y , color='red',height=0.3)
plt.show()