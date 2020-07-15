# works on iterable
# will have lambda as first parameter and iterable as second parameter
# lambda function will execute for each item in iterable
# it will return the list for which lambda function evaluates to true


scores = [45,25, 55, 14, 10, 5, 88, 99, 54, 66]
selected  = filter(lambda n: n>60, scores)
print((selected))
print(list(selected))


scores = [45,25, 55, 14, 10, 5, 88, 99, 54, 66]
alleven  = filter(lambda n: n%2 == 0, scores)
print((alleven))
print(list(alleven))

scores = [45,25, 55, 14, 10, 5, 88, 99, 54, 66]
allodd  = filter(lambda n: n%2 != 0, scores)
print((allodd))
print(list(allodd))


message = "abkra ka dabra ni ke meta checka"
vowels = 'aeiou'
#messagelist = list(message)
#vovellist = list(vowels)
#print(messagelist)
#print(vovellist)

checkvovelinmessage = filter(lambda alphabet: alphabet in list(vowels), list(message))
print(list(checkvovelinmessage))