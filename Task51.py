num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

# swapping the values if num1 is greater than num2

if num1 > num2:
    num1, num2, = num2, num1

sum_of_numbers = 0

for current_number in range (num1, num2 + 1):
    sum_of_numbers += current_number

print("the sum of all numbers between", num1, "and", num2, "is", sum_of_numbers)