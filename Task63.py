user_inputs = []

for i in range(3):
    number = int(input("enter a number:"))
    user_inputs.append(number)

def is_even(numbers):
    for number in numbers:
        if number %2==0:
            print(number, "is even")
        else:
            print(number,"is odd")

is_even(user_inputs)