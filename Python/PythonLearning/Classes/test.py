class Employee:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal

    def printinfo(self):
        print("#######%s Details###########" %self.name)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.sal)

    def modifyObject(self):
        self.name="Name of the employee"
        self.age="Age of the employee"
        self.sal="Salary of the employee"

class Person(Employee):
    pass
'''
Bhanu=Employee("Bhanu",31,'15lpa')
Bhanu.printinfo()
Rekha=Employee("Rekha",27,'5lpa')
Rekha.printinfo()

Bhanu.modifyObject()
Bhanu.printinfo()

'''

chandu=Person("Chandu",45,'30lpa')
chandu.printinfo()
chandu.age=31
chandu.sal='7lpa'
chandu.printinfo()
