newdict = {}
print(type(newdict))

days = {1:'monday', 2:'tuesday', 'three':'wed', 'others':['thu','fri', 7]}
print(type(days))
print(days)
#create dict from list of tuple
friends = list([("chennai", 8), ("japan", 22), ("bengaluru", 44)])
print(friends)
friendsdict = dict(friends)
print(friendsdict)
print(friendsdict['chennai'])
friendsdict.update({'chennai':88})
print(friendsdict['chennai'])
print(friendsdict)

#iterate through dict
for i,j in friendsdict.items():
    print(i + ": " + str(j))