string=input("Enter a string you want to reverse ")

n=len(string)
index=n-1

print("###########String in Reverse order##############")
for i in range(n):
    print(string[index-i],end="")
