from sys import argv

n=len(argv)

if(n>1):
    largest = eval(argv[1])

    for i in range(1,n):
        if eval(argv[i])>largest:
            largest=eval(argv[i])

    print("Largest Number is ",largest)
else:
    print("Please supply 3 Numbers")
    

