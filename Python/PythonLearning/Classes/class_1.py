class msg:
    def __init__(self,text):
        self.__txt=text
        
    def set(self,message):
        self.__txt=message

    def get(self):
        return self.__txt

    def reset(self):
        self.__txt=""


m=msg("Rekha")
name=m.get()
print("Name:",name)
m._msg__txt="chander"  ## This is private variable we cannot access it just by "m.__txt" we have to use "m._msg__txt"
print("Name:",m.get())
m.reset()
print("Name:",m.get())

