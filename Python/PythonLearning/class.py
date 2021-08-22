class Person:

    def __init__(self,name):
        self.name=name
        
    def talk(self):
        print(f"{self.name} is Talking")


Bhanu=Person("Bhanu")
chinna=Person("Chinna")
chinna.talk()
Bhanu.talk()
