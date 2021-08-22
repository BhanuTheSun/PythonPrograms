def add(x,y):
    result = lambda x,y: x+y
    print(type(result))
    return result(x,y)

result = add(2,3)
print(type(result))

print("Result",result)
