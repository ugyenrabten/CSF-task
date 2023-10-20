user_name = input("enter your name:")

vowels_count = 0
i = 0
while i < len(user_name):
    if user_name[i] in 'aeiou':
        vowels_count += 1
    i += 1

print("number of vowels:", vowels_count)