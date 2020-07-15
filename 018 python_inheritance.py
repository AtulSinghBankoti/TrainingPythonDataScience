class employee:
    #class attribute
    count = 0

    def __init__(self, fname, lname):
        print("In employee constructor!")
        self.fname = fname
        self.lname = lname
        employee.count += 1

    def getDetailParent(self):
        print(self.fname + " " + self.lname )

#fullstckengineer class is child of employee class
class fullstackenginner(employee):

    def __init__(self, fname, lname, tech):
        print("In fullstackengineer constructor!")
        self.tech = tech
        super().__init__(fname, lname)

    def getDetailChild(self):
        print(self.fname + " " + self.lname + " "  + self.tech)    


fse1 = fullstackenginner("CAS", "ML", "Java")        
fse1.getDetailParent()
fse1.getDetailChild()

e1 = employee("OWIO", "H")
e1.getDetailParent()

#__del__ e1


print(employee.count)
