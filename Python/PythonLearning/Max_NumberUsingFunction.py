def largest_number(list):
    max=list[0]
    for number in list:
        if number>max:        
            max=number
    return max

numbers=[13,5,7,8,2,10,14,5,7,4]
print("Actual List:" ,numbers)
max_number=largest_number(numbers)
print ("Largest Number in list is:", max_number)
