import random

secret_number = random.randint(1,100)

for i in range(3):
    guess = int(input("guess the secret number(1 and 100):"))
    if guess == secret_number:
        print("CONGRATULATIONS! You guessed the secret number", secret_number)
        break
    elif guess > secret_number:
        print("too high!")
    else:
        print("too low!")