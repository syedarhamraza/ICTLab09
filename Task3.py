import random
randomNumber = random.randint(1, 10)
while True:
    number = int(input("Guess a random number: "))
    if number == randomNumber:
        print("You guessed right!")
        break
    else:
        print("You guessed wrong!")