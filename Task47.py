user_number = int(input("please enter a number:"))
factorial = 1

for i in range(1, user_number + 1):
    factorial *= i

print("the factorial of", user_number, "is", factorial)