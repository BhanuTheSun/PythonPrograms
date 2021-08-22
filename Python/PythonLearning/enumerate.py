# Python program to illustrate 
# enumerate function in loops
indexes=["Bhanu","Chander","nagaraju"]
l1 = ["eat","sleep","repeat"] 
  
# printing the tuples in object directly 
temp_dict={indexes[index]:ele for index,ele in enumerate(l1)} 
print(temp_dict)
