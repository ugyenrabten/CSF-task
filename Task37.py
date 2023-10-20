# get the month from the user
month = input("enter a month:")

# check the month and print the corresponding season
if month == ("january" or "february" or "march" or "april" or "may"):
    print("spring")
elif month == ("june" or "july" or "august"):
    print("summer")
elif month == ("september" or "october" or "november"):
    print("fall")
elif month == ("december"):
    print("winter")
else:
    print("invalid month")