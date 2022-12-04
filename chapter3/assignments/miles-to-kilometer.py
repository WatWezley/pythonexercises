miles = int(input("Enter the miles: "))
print("Miles   Kilometer")
counter = 1
while counter <= miles:
    kilometer: float = counter * 1.69
    print(counter, "         ", kilometer)
    counter += 1
