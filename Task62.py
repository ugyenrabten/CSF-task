user_inputs = []

for i in range(3):
    number = int(input("enter a number:"))
    user_inputs.append(number)

def is_even(numbers):
    for number in numbers:
        if number %2!=0:
            return False
        return True
    
output = is_even(user_inputs)
print(output)