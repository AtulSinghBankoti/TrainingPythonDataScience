n1 = 8
print(n1)
print(type(n1))

#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(n1 + " is of type " + type(n1))
#TypeError: can only concatenate str (not "type") to str
#print(str(n1) + " is of type " + type(n1))

print(str(n1) + " is of type " + str(type(n1)))

n2 = 8.8
print(str(n2) + " is of type " + str(type(n2)))

#lists
mylist = []
print(type(mylist))
mylist_homo = [1,2,3,4,5,6,7,8]
mylist_hetero = [1,2,3,4,'Five', 'Six','G',8.88]
print(type(mylist_homo))
print(type(mylist_hetero))
#use contructor to create list
mylist_constru = list([1,2,3,4,'Five', 'Six','G',8.88, [1,2,3,4,5,6,7,8]])
print(type(mylist_constru))
#length of the list
print(len(mylist_constru))
print(len(mylist_homo))
#create python list by defining initial value for each element
new_list = [8] *4
print(new_list)
new_2dlist = [[4]*3]*3
print(new_2dlist)
print(new_2dlist[0][0])
#create new list by appending two lists (+ way and extend())
new_combined = mylist_homo + new_list
print(new_combined)
#using extend to add individual elements to list
l1 = [1,2,3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
#using append method
l1 = [1,2,3]
l2 = [4, 5, 6]
l1.append(l2)
print(l1)
#reverse indexing
vowels =['a','e','i','o','u']
print(vowels[0])
print(vowels[-1])
print(vowels[-2])

#slicing
mylist_homo = [1,2,3,4,5,6,7,8]
#[start:length_till_stop:step]
print(mylist_homo[1:5])
print(mylist_homo[1:6:2])
print(mylist_homo[4:1])
print(mylist_homo[4:-1])
print(mylist_homo[2:-1])
print(mylist_homo[:4])
print(mylist_homo[4:])
#reversing the list
print(mylist_homo[::-1])
print(mylist_homo[::-2])
print(mylist_homo[::-3])
#iterating the list
for value in mylist_constru:   
    print(value)
print(new_2dlist)
mylist_2dhomo = [[1,2,3],[4,5,6],[7,8,9]]
for x in mylist_2dhomo:
    for y in x:
        print(y, end=" * ")
    print()    


#some inbuilt methods
friend =['obb', 'cas', 'owioh', 'bnp']
print(friend)
print(friend.sort())
print(friend)