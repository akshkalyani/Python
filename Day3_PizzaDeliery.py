print("welcome to pizza delivery system")

size = input("What size of Pizza do you want S, M or L: ") #15,20,25
add_peparoni = input("Do you want pepperoni Y or N: ") #2
add_cheese = input("Do you want cheese Y or N: ") #3
bill = 0

if size=="S":
   bill=15
   if add_peparoni=="Y":
    bill +=1
elif size=="M":
    bill=20
    if add_peparoni=="Y":
     bill +=2
else:
    bill=25
    if add_peparoni=="Y":
     bill +=2

if add_cheese=="Y":
    bill += 1

print(f'The total bill is ${bill}')