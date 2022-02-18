import random

print("welcome to the love calculator !")

Your_name = input("Enter your name:")
their_name = input("Enter their name:")

# 
# ***************Randomised Love Score*****************
score = random.randint(0,100)

if score>=90 or score<=10:
    print(f"Your score is {score}, you go together like Coke and Mentos")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alrighty to-get-her")
else:
    print(f"Your score is {score}")