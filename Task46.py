user_number = int(input("please enter a number:"))
factorial = 1
counter = user_number

while counter > 0:
    factorial *= counter
    counter -= 1

print("the factorial of", user_number, "is", factorial)