my_tuple1 = tuple()
my_tuple2 = (1, 2, "obb", 22.88, ['a','x', 8])
print(type(my_tuple1))
print(type(my_tuple2))
my_tuple3 = 22, 44, 88
print(type(my_tuple3))
scores = [11, 22, 44]
checktuple  = tuple(scores)
print(checktuple)
#onlyone  = tuple(21)
onlyone = (21, )
print(onlyone)
#TypeError: 'tuple' object does not support item assignment
print(checktuple[0])
#checktuple[0]=12
addmetuple = [22,32, 442]
newtuple  =(5, 8, addmetuple)
print(newtuple)
for i in newtuple:
    print(i)