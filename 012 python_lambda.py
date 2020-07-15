def callMe(n1, n2):
    return n1 + n2

sum = callMe(4,6)    
print(sum)

#lambda function
message = lambda m: print(m)
message("Hello Lambda!!!!")


squared = lambda n: n*n
print(squared(4))

#multiple statements not possible in lambda.
#single statement will be returned by default!
cube = lambda n1, n2, n3: n1*n2*n3
print(cube(2,4,5))
""" 
def cube(n1, n2, n3):
    #statement 1
    #statement 2
    print("Something something")
    return n1*n2*n3    

print(cube(2,4,7))     """

#list of functions!

lambdaFunctionList = [lambda a: a**a, lambda a, b: a*b , lambda a,b=88: str(a)+ " " + str(b)]

#lambda a: a**a
print(lambdaFunctionList[0](4))

# lambda a, b: a*b
print(lambdaFunctionList[1](4, 5))

# lambda a,b: a+ " " + b
print(lambdaFunctionList[2](8, "SUPER EIGHT!!!!"))


# lambda a,b: a+ " " + b
print(lambdaFunctionList[2](8888, 44))


# lambda a,b: a+ " " + b
print(lambdaFunctionList[2](44))

# create list using lambda functions

