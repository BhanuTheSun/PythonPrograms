from sys import argv

def list_prime(m, n):
    for number in range(m, n+1):
        counter = 0
        for i in range(1, number+1):
            if(counter<3):   
                if number % i == 0:
                    counter += 1
        if counter == 2:
            prime_list.append(number)
    return prime_list

prime_list = []
m = int(argv[1])
n = int(argv[2])

if m<n:
    print("Prime Numbers in ", m, n, "range", list_prime(m, n))
else:
    print("Enter Proper Range ex: m should be less than n")
