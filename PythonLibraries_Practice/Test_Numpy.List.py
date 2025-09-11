import numpy as np

dtypes = [('name','S10'),('year',int),('cgpa',float)]

values = [('Ramu',2023,7.1),('Akash',2022,7.4),('Karthik',2024,6.9)]

arr1 = np.array(values ,dtype = dtypes)

print(arr1)

#Array sorted by names
print("\nArray sorted by names: \n",np.sort(arr1, order = 'name'))

#Array sorted by year
print("\n Array soretd by year : \n", np.sort(arr1 , order=['year','cgpa']))

