from collections import defaultdict

string="kdshfiuehfkjldjhkj"

n=len(string)
dictionary={}
for i in range(n):
    count=0
    for j in range(n):
        if(string[i]==string[j]):
            count+=1
            dictionary.update({string[i]:count})

print(dictionary)

maxvalue=max(list(dictionary.values()))

def findkey(maxval):
    for key,value in dictionary.items():
        if(value==maxvalue):
            return key

char=findkey(maxvalue)



#print("longest repeated character in given string is ",char)

key_list=list(dictionary.keys())
value_list=list(dictionary.values())

res=[(count,letter) for letter,count in zip(value_list,key_list)]

#print(res)
dict_char=defaultdict(list)


for key,value in res:
    dict_char[value].append(key)

len_dict=len(dict_char)
for i in dict_char.keys():
    if i==maxvalue:
        print("Longest repeated character ",dict_char[i])
        

#print(key_list)
#print(value_list)
#print(dict_char)


