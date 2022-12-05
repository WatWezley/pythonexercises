today = int(input("Enter a number 0-6 for today: "))
future = int(input("Enter number of days from the future: "))
future2 = future % 7
if today == 0:
    today = "Monday"
elif today == 1:
    today = "Tuesday"
elif today == 2:
    today = "Wednesday"
elif today == 3:
    today = "Thurday"
elif today == 4:
    today2 = "Friday"
elif today == 5:
    today = "Saturday"
elif today == 6:
    today = "Sunday"

if future2 == 0:
    future2 = "Monday"
elif future2 == 1:
    future2 = "Tuesday"
elif future2 == 2:
    future2 = "Wednesday"
elif future2 == 3:
    future2 = "Thursday"
elif future2 == 4:
    future2 = "Friday"
elif future2 == 5:
    future2 = "Saturday"
elif future2 == 6:
    future2 = "Sunday"
print(" Today is", today, "and the Future day is", future2)
