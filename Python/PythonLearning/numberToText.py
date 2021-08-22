numbers={
          "0":"Zero",
          "1":"one",
          "2":"two",
          "3":"Three",
          "4":"Four",
          "5":"Five",
          "6":"six",
          "7":"Seven",
          "8":"eight",
          "9":"Nine"
    }

phoneNumber=input("Enter your Phone Number:")

output=""
for digit in phoneNumber:
    output+=numbers.get(digit,"*")+" "

print (output)

