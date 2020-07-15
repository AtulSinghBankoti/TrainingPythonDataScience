myset  = { 4, 5, 6}
print(type(myset) )

#list -> ordered collection, [], use index position
#set -> unordered collection, does not allow duplicates, {}, cannot use index position

myset  = { 4, 5, 6, 4, 5, 6, 8, 9, 10, 12, 10, 13}
print(myset)

new_set1 = set()
new_set2 = { }
print(type(new_set1))
print(type(new_set2))

#TypeError: 'set' object is not subscriptable
#print(myset[0])

new_set1 = {1,2,3,4,5,6,7,8}
new_set2 = {6,7,8,9,10}

print(new_set1.union(new_set2))
print(new_set1.intersection(new_set2))
#new_set1 - new_set2
print(new_set1.difference(new_set2))
#new_set2 - new_set1
print(new_set2.difference(new_set1))

for i in new_set2:
    print(i, end=" ")

print()
#check if value is present in set!
print(4 in new_set1)    
print(4 in new_set2)   

new_set2.add(11)
print(new_set2)

new_list1 = [1,2,3,4,5,6,7,8]
print(4 in new_list1)

#frozen set
fs = frozenset(new_set2)
print(type(fs))
#cannot modify frozen set!