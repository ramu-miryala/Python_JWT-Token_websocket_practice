import numpy as np

a = np.array([1, 2, 3])
b = np.array([[10],[20]])
print(a + b)

c = np.array([0, np.pi/2, np.pi])
print(np.sin(c))  # Output: [0.         1.         0.]

A = np.array([[1, 2], [3, 4]])
B = np.linalg.inv(A)  # Inverse of matrix A
print(B)

rand_array = np.random.rand(3, 2)  # 3x2 array with random values between 0 and 1
print(rand_array)

# Solving linear equations Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)