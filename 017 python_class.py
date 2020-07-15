"""
Class

1. class keyword
2. instance attributes
3. class attributes
4. __init__ method -> contructor
5. self -> refers tot he instance of the class

"""

class employee:
    # count is class attribute
    count = 0
    def __init__(self, name, location):
        #name and location are instance attributes!
        self.name = name
        self.location = location
        print("constructor called!!!!")
        employee.count+=1

    def printEmployee(self):
        print(self.name + " from " + self.location)


e1 = employee("obb", "chennai")        
e2 = employee("cas", "mumbai")
e3= employee("owioh", "japan")
e1.printEmployee()
e2.printEmployee()
e3.printEmployee()

print("Count of employees: " + str(employee.count))