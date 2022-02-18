height = float(input("Enter your height in M:"))
weight = float(input("\nEnter your weight in KG:"))

bmi = round(weight/(height**2))

if bmi<=18.5:
    print("Your BMI is " + str(bmi) + ", you are underweight")
elif bmi<=25:
    print("Your BMI is " + str(bmi) + ", you have a normal weight")
elif bmi<=30:
        print("Your BMI is " + str(bmi) + ", you are overweight")
elif bmi<=35:
        print("Your BMI is " + str(bmi) + ", you are obese")
else:
        print("Your BMI is " + str(bmi) + ", you are clinically obese")



