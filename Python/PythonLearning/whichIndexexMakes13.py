mylist=[10,11,12,13,0,7,6,14,-1,21,-7]

n=len(mylist)

print(n)

for i in range(n):
  for j in range(n):
    if(mylist[i]+mylist[j]==13):
        print("Index %d and Index %d makes 13 "%(i,j))
    
