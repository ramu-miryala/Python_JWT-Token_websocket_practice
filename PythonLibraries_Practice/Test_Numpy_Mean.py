import numpy as np
from scipy import stats

data =[1,2,3,4,5,6,7,8,93,4,79,2,4,6]

#mean value of data
mean_value = np.mean(data)
print("Mean ",mean_value)

#mode value of data
mode_value = stats.mode(data, keepdims=True)
print("Mode ",mode_value.mode[0],"( count:" ,mode_value.count[0],")")

#standard deviation of data
std_dev = np.std(data)
print("Standard Deviation: ", std_dev)
