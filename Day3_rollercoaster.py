from tkinter import Y


height = int(input("What is your height in CM:"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age:"))

    if age>=18:
        if age>=45 & age<=55:
            bill = 0
            print("The estimated ticket fare would be $0")
        else:
            bill = 12
            print("Ticket fare would be $12")
    elif age>=45 & age<=55:
        bill = 0
        print("The estimated ticket fare would be $0")
    elif age>12:
        bill = 7
        print("The estimated ticket fare would be $7")
    else:
        bill = 5
        print("The estimated ticket fare would be $5")

    photo = input("Do you want photos Y/N(Y for yes N for No):")
    if photo=="Y" or photo=="y":
        bill = bill + 3
        print(f"The total bill is {bill}")


else:
    print("you need to grow tall")

