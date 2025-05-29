price = int(0)
RED = '\033[31m'
RESET = '\033[0m'
BRIGHT_BLACK   = "\033[90m"
BRIGHT_RED     = "\033[91m"
BRIGHT_GREEN   = "\033[92m"
BRIGHT_YELLOW  = "\033[93m"
BRIGHT_BLUE    = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN    = "\033[96m"
BRIGHT_WHITE   = "\033[97m"
import random
import sys
 
 
def welcome():
    print("----Hello, welcome to the fancy appartments----\n")
   
    floor_num = int(input("Please input a floor number (0-245) --> "))
    print("")
    app_num = int(input("Please enter the appartment number of the appartment you desire to stay at (0-625) --> "))
    print("")
 
    resident_num = (floor_num*2) + app_num
 
    # Filled Appartments
    app_taken = random.randint(1, 100)
    app_taken2 = random.randint(1, 100)
    app_taken3 = random.randint(1, 100)
    app_taken4 = random.randint(1, 100)
    app_taken5 = random.randint(1, 100)
    app_taken6= random.randint(1, 100)
    app_taken7 = random.randint(1, 100)
    app_taken8 = random.randint(1, 100)
    if app_num == app_taken:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken2:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken3:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken4:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken5:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken6:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken7:
        print("Sorry appartment filled, look again.")
        sys.exit()
    if app_num == app_taken8:
        print("Sorry appartment filled, look again.")
        sys.exit()
 
    if app_num > 625:
       app_num = "We don't have that mamy appartments on that floor, please redo order"
 
    if floor_num > 0:
        price = 345.79
    elif floor_num > 10:
        price = 549.99
    elif floor_num > 50:
        price = 2954.99
    elif floor_num > 245:
       print("We don't have that many floors, please redo order")
    else:
        print("Error, please contact support")      
   
    print(f"The price of your appartment per month is {price}\n")
 
    paying = input("Do you wish to complete your transacion? (Y/N) --> ").upper()
    print("")
 
    if paying == "Y":
     print(f"-You are renting appartment number: {app_num}- \n -Your appartment is on floor: {floor_num}- \n -Cost per month is: ${price}- \n -Your resident number is: {resident_num}- \n")
     print("----ENJOY YOUR APPARTMENT!----\n")
    elif paying == "N":
     print("--Sorry to hear that, have a good day!----")
    elif paying == "U":
       begining()
    else:
       print("Not a valid input, but if you want to stay here you can play the guessing game...")
 
welcome()
 
 
 
def begining():
    choice_1=input(RED + "Are you ready to play the game!? (N/Y) --> " + RESET).upper()
    if choice_1 == "y".upper():
        Run()
    elif choice_1 == "n".upper():
        print("Okay, bye")
    else:
        print("Not what I asked for...")
 
def Run():
    chosenNum = random.randint(1, 100)
    for i in range(6):
        imp = int(input(BRIGHT_GREEN+'pick a number: '+RESET))
        if imp > chosenNum:
            print(BRIGHT_YELLOW+'Go Lower!'+RESET)
        elif imp < chosenNum:
            print(BRIGHT_CYAN+'Go Higher!'+RESET)
        else:
            print(BRIGHT_MAGENTA+'GOOD JOB'+ RESET)
            return
        if i + 1 == 6: print(BRIGHT_RED+'You Failed...'+RESET)
 
 
