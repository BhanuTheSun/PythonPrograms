class Dummy:
    count=0
    def __init__(self):
        Dummy.count+=1

    def __del__(self):
        Dummy.count-=1

    @staticmethod
    def get_count():
        return Dummy.count


d1=Dummy()

print(Dummy.get_count())

d2=Dummy()

print(Dummy.get_count())

del d1

print(Dummy.get_count())

del d2

print(Dummy.get_count())
