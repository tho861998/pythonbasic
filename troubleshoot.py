print("Help! My computer doesn't work!")
print("Does the computer make any ")
choice = input("or show any lights? (y/n): ")
if choice == 'n':
    choice = input("Is it plugged in? (y/n): ")
    if choice == 'n':
        print("Plug it in. If the problem persists,")
        print("Please run this program again.")
    else: #plug in
        choice = input("Is switch in the \"on\" position? (y/n): ")
        if choice == 'n':
            print("Turn it on. If the problem persists: ")
            print("Run the program again")
        else: #switch is on
            choice = input("Does this computer has a fuse? (y/n): ")
            if choice == 'n': #no fuse
                choice = input("Is the outlet OK? (y/n): ")
                if choice == 'n':
                    print("check outlet's circuit")
                else:
                    print("Please consult a service technician.")
            else: #check fuse
                print("check the fuse. Replace if")
else:
    print("Please consult a service technician.")
