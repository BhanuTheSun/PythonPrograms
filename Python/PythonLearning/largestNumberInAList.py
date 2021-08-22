numbers=[2,6,5,9,4,5,10,13]

def largest_number(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:        
            largest=number
    return largest

print (numbers)
print ("Largest Number in a list is = ",largest_number(numbers))
    
    
