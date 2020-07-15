#reduce

# it is a aggregator function
# works with iterable
# returns single value

from functools import reduce

scores = [1,2,3,4,5]

total = reduce(lambda n1, n2: n1+n2, scores)
print(type(total))
print(total)


total = reduce(lambda n1, n2: n1*n2, scores)
print(type(total))
print(total)

scores = [22, 45, 88, 99, 12, 47, 55]
max = reduce( lambda n1, n2: n1 if n1>n2 else n2 , scores)
print(max)

min = reduce( lambda n1, n2: n1 if n1<n2 else n2 , scores)
print(min)


#chaining filter, map and reduce!
numbers = [5, 10, 15, 4, 2, 8, 7, 3, 6]
#get the sum of square of all number less than 5

def sumNo(a, b):
    return a+b

def squareNo(c):
    return c*c

def lessThan(d):
    if(d<5):
        return True
    else:
        return False    


sum = reduce(sumNo, map(squareNo, filter(lessThan, numbers)) )
print(sum)


sum = reduce(lambda a,b: a+b, map(lambda a:a*a, filter(lambda a:a<5, numbers)) )
print(sum)

sumSqEven = reduce(lambda a,b: a+b, map(lambda a:a*a, filter(lambda a:a%2 == 0, numbers)) )
print(sumSqEven)

