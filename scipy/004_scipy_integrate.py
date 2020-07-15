import scipy.integrate

f1 = lambda x:x**2

#to get integration of function f1 with lower limit = 0 and higer limit = 1

getme = scipy.integrate.quad(f1, 0, 1)
print(getme)