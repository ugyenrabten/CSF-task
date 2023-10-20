user_name = input("please enter your name:")
vowels = "aeiouAEIOU"

for char in user_name:
    if char in vowels:
        print(True)
        break
else:
    print(False)