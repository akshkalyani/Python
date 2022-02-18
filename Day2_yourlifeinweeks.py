age = input("What is your current age: ")

age = int(age)
days = 90*365 - age*365
months = 90*52 - age*52
years = days/365



print(f"If you were to live 90 years then the number of \nDays: {days},\nMonth: {months},\nYears: {years}")