#SYED ARHAM RAZA 2430-0159
import random
randomNumber = random.randint(1, 10)
while True:
    number = int(input("Guess a random number: "))
    if number == randomNumber:
        print("WIN!")
        break
    else:
        print("LOSE!")
