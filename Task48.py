import random
secret_number = random.randint(1,100)
guess = int(input("guess the secret number(between 1 and 100):"))

while guess != secret_number:
    if guess > secret_number:
        print("too high!")
    else:
        print("too low!")
    guess = int(input("guess again:"))

print("CONGRATULATIONS! You guessed the secret number", secret_number)