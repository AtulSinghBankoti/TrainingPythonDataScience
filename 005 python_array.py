import array as ary

#create an array of integers
array_scores = ary.array('i', range(10))
print(array_scores)
print(type(array_scores))

array_scores = ary.array('i', range(10, 21))
print(array_scores)
print(type(array_scores))


#iterating through array
for i in array_scores:
    print(i,  end=" ")