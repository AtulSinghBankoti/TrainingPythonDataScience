import scipy.special
import numpy as np

a = np.arange(10)
print(a)
print("Get cube root of each element in a: ")
print(scipy.special.cbrt(a))

print("Get permutation when r elements are arranged from total of n elements - order matters:")
# nPr = n! / (n-r)!
getme = scipy.special.perm(3, 2)
print(getme)
getme = scipy.special.perm(5, 2)
print(getme)

print("Get combination when r elements are combined from total of n elements - order does not matter:")
# nCr = n! / (r!)(n-r)!
getme = scipy.special.comb(5, 2)
print(getme)