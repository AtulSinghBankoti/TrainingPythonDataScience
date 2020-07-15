# map will work only with iterables
# it will always return the list 
# map will use "lambda function" as first parameter and iterable as second parameter
# lambda function will have (iterate on) one parameter, which will be one item of iterable

friends =['obb', 'cas', 'owioh', 'bnp']
scores = [1,2,3,4,5,6,7,8,9,10]

whoami = map(lambda n: n, friends)

print(type(whoami))
print(list(whoami))

squared =  map(lambda n: n*n , scores)
print(type(squared))
print(list(squared))

def squareme(n):
    return n*n

squared =  map(squareme , scores)
print(type(squared))
print(list(squared))

rollnumber = [1,2,3]
english = [22, 35, 44]
maths = [10, 20, 30]
total = map(lambda rn, e, m: str(rn)+':'+str(e+m) , rollnumber, english, maths)
print(type(total))
print(list(total))




rollnumber = [1,2,3, 4, 5, 6, 7, 8, 9, 10]
english = [22, 35, 44, 55, 10, 78]
maths = [10, 20, 30, 45]
total = map(lambda rn, e, m: str(rn)+':'+str(e+m) , rollnumber, english, maths)
print(type(total))
print(list(total))

message = 'hello'
print(list(message))

messages = ['Help', 'Ok', 'Horn Ok Please', 'Drive safe']
messageslist = map(list , messages)
print(list(messageslist))