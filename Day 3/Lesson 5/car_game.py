#--------------------------- version 1 ---------------------------
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car start...")
    elif command == "stop":
        print("Car stop.")
    elif command == "help":
        print("""
        start = to start the car
        stop = to stop the car
        quit = to quit
        """)
    elif command == "quit":
        print("Good bye, See you next time")
        break
    else:
        print("Sorry, I don't understand that!!!")



#--------------------------- version 2 ---------------------------
command = ""
Started = True
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car start...")
    elif command == "stop":
        print("Car stop.")
    elif command == "help":
        print("""
        start = to start the car
        stop = to stop the car
        quit = to quit
        """)
    elif command == "quit":
        print("Good bye, See you next time")
        break
    else:
        print("Sorry, I don't understand that!!!")