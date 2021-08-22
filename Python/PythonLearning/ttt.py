from sys import argv


prime_list = []
def list_prime(m, n):
    for number in range(m, n+1):
        counter = 0
        for i in range(1, number+1):
            if number % i == 0 and counter <3:
                counter += 1                
        if counter == 2:
            prime_list.append(number)
    return prime_list

print(list_prime(1,20))
