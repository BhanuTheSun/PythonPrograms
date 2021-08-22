print ("This is a car game Enter Help if you need any Assistance!!")
car_started=False
while True:

    command = input().lower()
    if command == "start":
        if car_started:
            print("Car is already started")            
        else:
            car_started=True
            print("car started...Lets Go")
                    
    elif command == "stop":
        if not car_started:
            print("car is already stopped")            
        else:            
            car_started=False
            print("car stopped")        
    elif command == "help":
        print (''' 
Start --> Type Start to Start the car
Stop ---> Type Stop to Stop the car
quit ---> Type quit to quit the game
''')
    elif command == "quit":
        quit_choice=input("Are you sure? y/n")
        if quit_choice.lower()=="y":
            break
        else:
            print("Play the Game")
    else:
        print ("I didn't understand your command please type help and check available commands from the list and comeback....")
