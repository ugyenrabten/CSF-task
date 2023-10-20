score = int(input("enter your score:"))
if not score == (0 <= score <= 100): #assuming the score should be between 0 to 100
    print("invalid score")
if 100 == score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
if score < 60:
    print("F")
