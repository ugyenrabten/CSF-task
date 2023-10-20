num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

# swapping the values if num1 is greater than num2

if num1 > num2:
    num1, num2, = num2, num1

sum_of_numbers = 0
current_number = num1

while current_number <= num2:
    sum_of_numbers += current_number
    current_number += 1

print("the sum of all numbers between", num1, "and", num2, "is", sum_of_numbers)