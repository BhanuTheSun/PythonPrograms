list=[10,5,7,9,4,5,3,2,8]
list.sort()
largest=list[0]
second_largest=list[0]
for number in list:
    if number>largest:
        largest_index=list.index(number)
        largest=number
        second_largest=list[largest_index-1]

print (list)
print ("Largest Number in a list is = %d" %largest)
if largest == second_largest:
    print ("Largest and Second_largest are same = %d" %largest)
else:
    print ("Second Largest Number in a list is = %d" %second_largest)
    
    
