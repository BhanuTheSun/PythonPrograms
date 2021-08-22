class Employee:
    count=0
    def __init__(self,empname,empid):
        self._name=empname
        self.__id=empid
        Employee.count+=1
    def display_employee(self):
        return (self._name,self.__id)
    @staticmethod
    def total_instances():        
        return Employee.count

    
emp1=Employee("Bhanuchander",308567)
print(emp1.display_employee())
print("Total Number of instances created for the Employee class:",Employee.total_instances())
