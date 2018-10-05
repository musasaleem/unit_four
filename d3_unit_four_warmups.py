grade = int(input("What grade are you in"))


if grade > 0 and grade < 6:
    print("You are in lower school")

elif grade > 5 and grade < 9:
    print("You are in middle school")

else:
    print("You are in high school")