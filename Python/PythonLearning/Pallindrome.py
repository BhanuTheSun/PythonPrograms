n=int(input("Enter a number: "))
temp=n
rev=0
print(rev)
while n>0:
    number=n%10
    rev=rev*10+number
    n=n//10

print(rev)
print(temp)
if(rev==temp):
    print(f"Number {temp} is pallindrom")
else:
    print(f"Number {temp} is not a pallindrom")


