secret_number=9
attempts=3
while(attempts>=1):
    guessed_number = int(input(f"Guess what is the secret number (you have {attempts} attempts):"))
    if guessed_number == secret_number:
        print("You Won the Game")
        break
    attempts-=1
else:
    print ("You Lost the Game")
