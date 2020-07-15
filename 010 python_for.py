for i in range(10):
    print(i, end=' ')

print()

for i in range(10, 20):
    print(i, end=' ')

print()    
for i in range(10, 20, 2):
    print(i, end=' ')

print()
# exponent operator **
for i in range(1, 10):
    print(str(i) + "  to power of " + str(i) + " = " + str(i**i))    
else:
    print("Exponent of 1 to 9 is done!!!!")    

for i in range(1, 10):
    print(str(i) + "  to power of " + str(i) + " = " + str(i**i)) 
    if(i  == 4):
        break
else:
    print("Exponent of 1 to 9 is done!!!!")        