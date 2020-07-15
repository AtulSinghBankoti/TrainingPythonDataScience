name = "abkRa KA DabrA"
print('a' in name)
print('z' in name)
print('D' not in name)
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.swapcase())
print(name.count('ab'))
print(name.count('a',0, 5))

for a in name:
    print(a, end=", ")

print()
newname = name[0:5]    
print(newname)

newname = name[::-1]    
print(newname)

language = "malayalam8"
ulta = language[::-1]
print(language + ' palindrome ' + ulta )
