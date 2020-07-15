"""
File IO

1. Open the file in specific mode
2. Receive the file handle.
3. Use file handle for file operations (red, write, change, delete)
4. Close the file handle.

"""
print("Opening the file: ")
fh = open("001 hello_world.py", "r" )
print(fh)
print(fh.mode + " " + fh.name)
print("File is open: " + str(not(fh.closed)))
fh.close()
print("File is open: " + str(not(fh.closed)))

#write to file
print("Writing to file: ")
with open("intro.txt", "w") as fh1:
    fh1.write("Hello from Python FILE IO!!!! \n")
    fh1.write("This is new line! \n")
    fh1.write("-----------------------------------------")
    print("File is open: " + str(not(fh1.closed)))
print("File is open: " + str(not(fh1.closed)))    



#append to file
with open("intro.txt", "a") as fh:
    fh.write("\n")
    fh.write("I need new line explicitly!!!! \n")
    fh.writelines("How will be be written? \n")
    fh.write("Check me now!!!!")

#read from file

with open("intro.txt", "r") as fh:
    content = fh.readlines()
    print(content)
    for eachline in content:
        print(eachline)

#read chunks from file

with open("intro.txt", "r") as fh:
    content1 = fh.read(10)
    content2 = fh.read(10)
    print(content1)
    print(content2)
    print(fh.tell())
    print(fh.read(5))
    print(fh.tell())
    print(fh.read(4))
    print(fh.tell())
    fh.seek(11)
    print(fh.read(12))

#copy data from one file to another
with open("intro.txt", "r") as fh:
    content = fh.readlines()
    with open("target.txt", "w") as fhw:
        for eachline in content:
            fhw.write(eachline)


#copy data from one image to another
with open("python.png", "rb") as fh:
    content = fh.readlines()
    with open("mypython.png", "wb") as fhw:
        for eachline in content:
            fhw.write(eachline)
    