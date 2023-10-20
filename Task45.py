user_name = input("enter your name:")

vowels_count = 0

for char in user_name:
    if char in "aeiou":
        vowels_count += 1
print("number of vowels:", vowels_count)