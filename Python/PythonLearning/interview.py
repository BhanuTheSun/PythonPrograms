'''
string=str(12345678910)
print(string)
list1=list(string)
print(list1)
n=len(list1)
for i in range(n-1):
    print(i)
    if(list1[i]==str(5)):
        del list1[i]
for i in list1:
    print(i,end="")

'''

'''
num=12345678910
res=[int(x) for x in str(num)]
print(type(res[0]))
string=""
for i in res:
    print(i)
    if(i==1):
        continue
    string+=str(i)
print(string)

'''

'''
x=[1,2,3,4,5]
list1=[x*2 for i in x]  ####### This statement is similar to  below one
#for i in x:
#    print(x*2)
print(list1)
'''

'''
mylist=[10,11,12,13,0,7,6,14,-1,21,-7]

n=len(mylist)

for i in range(n):
  for j in range(n):
          if(mylist[i]+mylist[j]==13):
              print("Index %d and Index %d makes 13 "%(i,j))
    
'''

# input 24356786
#  print largest two digit number
#  ex: here 86 is the largest number.

'''


'''
# input [17,10,7,5,12,11,6,3,4,7,8,0,1,2,3]
#  logic leaving first element of the array which two numbers addition becomes first element
#  print those two number as below
#  output: 10,7 5,12 11,6
'''
'''
# input [1,0,0,0,2,0,0,2] or [2,0,0,0,2,1,0]
# lowest distance of 2 from 1 shoud be returned
'''
'''
