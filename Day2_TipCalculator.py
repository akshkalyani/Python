print("Welcome to the tip calculator")
bill_amt = input("What is the total amount of bill?")
tip_percentage = input("What percentage tip you would like to give?")
people = input("How many people to split the bill?")

tip_amt = (float(bill_amt)*float(tip_percentage))/100 
total_bill = float(tip_amt) + float(bill_amt)
each_pay = float(total_bill)/float(people)
each_pay = round(each_pay, 2)
#print(f"Each person will pay {each_pay}")
print("Each person will pay",each_pay) #this also works of you do not want to use f-string