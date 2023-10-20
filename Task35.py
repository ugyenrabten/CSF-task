day = input("enter the day:")
if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday":
    print("weekday")
elif day == "friday":
    print("TGIF")
elif day == "saturday" or day == "sunday":
    print("weekend")
else:
    print("invalid input")