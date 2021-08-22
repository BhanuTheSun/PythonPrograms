try:
    a=10
    b=20
    c=a/b
except ZeroDivisionError as e:
    print("ZeroDivisionError",e)

except Exception as error:
    print("All kind of Exceptions",error)
else:
    print("There is no exception")
finally:
    print("Finally gets executed even if there is any exception or no exception is raised by try block")
