price = int(0)
def welcome():
    print("----Hello, welcome to the fancy appartments----\n")
    
    floor_num = int(input("Please input a floor number (0-245) --> "))
    print("")
    app_num = int(input("Please enter the appartment number of the appartment you desire to stay at (0-625) --> "))
    print("")

    resident_num = (floor_num*2) + app_num

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
    else:
       print("Not a valid input")

welcome()
