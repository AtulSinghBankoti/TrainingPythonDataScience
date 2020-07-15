# x + y = 2
# x + 3y = 9

# 1. convert linear algebra function into matrices!

import scipy.linalg
import numpy as np

a = np.array([[1,1,],[1,3]])
b = np.array([2, 9])
print("Get value of x and y")
print(scipy.linalg.solve(a ,b ))
print("Matrix a")
print(a)
print("Determinant of matrix a")
print(scipy.linalg.det(a))
"""
[a b]
[c d]
det = ad - bc
"""
print("Inverse of matrix a")
print(scipy.linalg.inv(a))
