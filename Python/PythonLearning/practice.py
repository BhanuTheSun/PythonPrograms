lst=[1,4,7,8,9,10,11,14,16,17]
lst.sort()
print(lst)
n=len(lst)
large=lst[0]
for i in range(n):
    if(lst[i]>large):
        large=lst[i]
        second_large=lst[i-1]

print(large)
print(second_large)
