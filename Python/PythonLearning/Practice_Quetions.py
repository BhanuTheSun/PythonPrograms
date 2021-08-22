#########0 1 1 2 3 5 8 13 21 34###########################

'''
f0=0
f1=1

n=int(input("Enter length of the fibonaci series "))

print("#######Fibonaci series#########")
print(f0,f1,end=" ")
for i in range(n-2):
    f2=f0+f1
    f0=f1
    f1=f2
    print(f2,end=" ")
'''
############Reverse of a string###########################
'''
string=input("Enter a string to be reversed: ")

def stringrev(mystring):
    string=mystring[::-1]
    return string

print("Reversed string ",stringrev(string))
'''
'''
string=input("Enter a string to be reversed: ")

n=len(string)

for i in range(1,n+1):
    print(string[n-i],end="")
'''


############aaaaabbbbbccccczzzzzffff##########find which character is repeated most of the time and print it
'''
string=input("Enter a string ")

n=len(string)
elements={}

for i in range(n):
    counter=0
    for j in range(n):
        if(string[i]==string[j]):
            counter+=1

        elements.update({string[i]:counter})

print(elements)

maxvalue=max(elements.values())
for key,value in elements.items():
    if(value==maxvalue):
        print(key)

'''
#########################decorator########################################
'''
#######decorator#######

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

pretty=make_pretty(ordinary)
pretty()

'''
#######################Reverse of a string using Generators##############
'''
def rev_str(string):
    n=len(string)
    for i in range(n-1,-1,-1):
        yield string[i]

val=rev_str("Bhanu")
print(next(val))
#for char in rev_str("Bhanu"):
#    print(char,end="")
'''
####################################input=paragraph,output=number of pallindrom words which are unique##################
'''
function should accept a paragraph which may contain multiple lines,multiple sentenses, multiple words
return count of unique pallindrom words in a paragraph
1) reverse given paragraph of words
2) eliminate duplicate words
3) return number of unique pallindrom words in a given paragraph
'''
'''
def pallindrom(para):
    input_str=para.lower()
    original_word_list=input_str.split()
    rev_word_list=[]
    for word in original_word_list:
        if word not in rev_word_list:
            rev_word_list.append(word[::-1])
    length=len(rev_word_list)
   
    count=0
    for i in range(length):
        if(original_word_list[i]==rev_word_list[i]):
            count+=1
    print(original_word_list)
    print(rev_word_list)
    return count
    

string="Malayalam is a super language, Madam told me, mom is preparing food working on learning python, Malayalam is great language"
print(pallindrom(string))

'''

###################################input=list of values, output=output_list which has 1's and 0's as explained below##################################


'''
function should take list as input ,find out elements of this list are present in fibonaci series if yes add 1 to the list if no add 0 to the list
and return list of 1's and 0's
exaples:::: input_list=     [1,4,6,8,9,10,13,21,34,18]
            fibonaci_series=[1,2,3,5,8,13,21,34,...] 
            output_list=    [1,0,0,1,0,0,1,1,1,0]   this list has to be returned.
'''
'''
def find_element_exists(input_list):
    fibonacci_series=[1,2,3,5,8,13,21,34,55,89]
    n=len(input_list)
    output_list=[]

    for i in input_list:
        if i in fibonacci_series:
            output_list.append(1)
        elif i not in fibonacci_series:
            output_list.append(0)
        
    return output_list

input_list=[1,4,6,8,9,10,13,21,34,18]
result_list=find_element_exists(input_list)
print(result_list)
'''

############################################################################################################################################################
'''
input1=list[intergers]
input2=integer

output: return type_of_series,[N-1,N,N+1]

ex:we have to find input provided is Arithmetic Progression or Geometric Progression and store it in "type_of_series" use input2 to find Nth term.
      using it find N-1,N,N+1 terms.

Arithmetic progression:  ex: 1 4 7 10 13 16 ....

nth term formula: Tn=a1+(n-1)*d
where a1 = first term( a1=1)
      n  = term number (is it 4th or 5th or...)
      d  = common difference (i.e. 4-1=3 and 7-4=3 so d=3)

      if we need 7th term 1+(7-1)*3=19

      if we need 10th term  1+(10-1)*3 = 28
Geometric Progression:  ex: 5 25 125 625 ....

                         (n-1)
nth term formula: Tn=a1*r     ( a1* r tothe power of (n-1))
where      a1=first term( a1=5)
           n=term number
           r=common difference (i.e. 25/5=5; 125/25=5 r=5)
'''

'''
def progression(input1,input2):
    
    n=len(input1)
    #print("n",n)
    Acount=Gcount=0
    d=input1[1]-input1[0]
    r=int(input1[1]/input1[0])
    #print("d= ",d)
    #print("r= ",r)
    term_list=[]
    i=0
    while(i<n-1):
        if(input1[i+1]-input1[i]==d):
            Acount+=1
        elif(int(input1[i+1]/input1[i])==r):
            Gcount+=1
        i+=1

    #print(Acount)
    #print(Gcount)
    if(Acount>=n-2):
        #print ("It is Arithmetic Progression")
        type_of_series="Arithmetic"
        tn=int(input1[0]+(input2-1)*d)     # a1+(n-1)*d
        #print("%dth term in given series is " %(input2,tn))
        t1=tn-d
        t2=tn
        t3=tn+d
    if(Gcount>=n-2):
        #print ("It is Geometric Progression")
        type_of_series="Geometric"
        tn=int(input1[0]*pow(r,input2-1))   # a1*r tothe power of (n-1)
        #print("%dth term in given series is %d" %(input2,tn))
        t1=int(tn/r)
        t2=tn
        t3=tn*r
    term_list=[t1,t2,t3]
    return (type_of_series,term_list)


type_of_series,list_of_Nterms=progression([1,4,7,10,13,16],8)

print("Type of Series = ",type_of_series)
print("Nterms = ",list_of_Nterms)


'''





















