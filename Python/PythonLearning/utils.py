def second_largest(list):
    list.sort()
    largest=list[0]
    second_largest=list[0]
    for number in list:
        if number>largest:
            largest_index=list.index(number)
            largest=number
            second_largest=list[largest_index-1]
    return second_largest

def largest_number(list):
    max=list[0]
    for number in list:
        if number>max:        
            max=number
    return max

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def square(x):
    return x*x
