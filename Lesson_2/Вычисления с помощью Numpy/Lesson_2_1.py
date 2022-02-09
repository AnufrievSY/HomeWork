import numpy as np

a = np.array([[1, 2, 3, 3, 1],
             [6, 8, 11, 10, 7]])
a = a.T
mean_a = np.mean(a, axis=0)

print(mean_a)
