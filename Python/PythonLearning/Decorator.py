def is_called():
    def is_returned():
        print("Hello")
        var=3
    return is_returned

new= is_called()

print(type(new))

#Outputs "Hello"
new()
