numbers=[0,1,4,5,7,2,3,9,5,4,2]
uniqueList=[]

for item in numbers:
    if item not in uniqueList:
        uniqueList.append(item)

print ("original List = ", numbers)
print ("After Removing Duplicates", uniqueList)
