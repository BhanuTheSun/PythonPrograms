class Emp:
    empCount=0
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal
        Emp.empCount+=1
    
    def employeeCount():
        return Emp.empCount

    def displayEmp(self):
        print("Name: ",self.name," Salary: ",self.salary)


emp1=Emp("Bhanu",10000)
emp2=Emp("Rekha",5000)

print("Total Employees in organisation ",Emp.employeeCount())
print("Employee Details")
emp1.displayEmp()
emp2.displayEmp()

setattr(emp2,'Age',31)

if (hasattr(emp2,'Age')):
    print("Age attribute is present in Emp class")
else:
    print("Age Attribute is not present in Emp class")

print("New Attribute added to emp2 object", getattr(emp2,'Age'))

delattr(emp2,'Age')

print("class name: ",Emp.__name__)
print("Documentation String: ",Emp.__doc__)
print("Base Classes: ",Emp.__bases__)
print("Module name in which Emp class is presetn: ",Emp.__module__)
print("variables and functions in current namespace: ",Emp.__dict__)
print("weakref attribute: ",Emp.__weakref__)
print("Emp1 belongs to : ", emp1.__class__.__name__)



