import random

input("welcome to cointoss\n\nWhat do you chose:")
random_out = int(random.randint(1,3))
if random_out==1:
    print("Its, a Head")
else:
    print("Its, a Tale")
