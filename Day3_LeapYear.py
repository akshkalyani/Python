year = int(input("Enter a year:"))
if year%4==0:
    
    if year%100!=0:
     print("Its a leap year")
    
    elif year%400==0:
     print("Its a leap year")
           
    else:
        print("The year is not a leap year")
else:
    print("The year is not a leap year")
       