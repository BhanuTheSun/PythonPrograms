string="aabbbcccdddpzzppppaaaaaazzzzzzzzaaaa"

ac=bc=cc=dc=pc=zc=pc=0
n=len(string)
for i in range(n):
  if(string[i]=='a'):
    ac+=1
  elif(string[i]=='b'):
    bc+=1
  elif(string[i]=='c'):
    cc+=1
  elif(string[i]=='d'):
    dc+=1
  elif(string[i]=='p'):
    pc+=1
  elif(string[i]=='z'):
    zc+=1

characters=['a','b','c','d','p','z']
counters=[ac,bc,cc,dc,pc,zc]

dictionary=dict(zip(counters,characters))
print(dictionary)

large=counters[0]
length=len(counters)
for i in range(length):
  if(counters[i]>large):
    large=counters[i]
    
print("Character which makes longest repetation is ",dictionary[large])
