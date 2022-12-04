kilogram = int(input("Enter the kilogram: "))
print("Kilogram   Pounds")
counter = 1
while counter <= kilogram:
    pounds: float = counter * 2.2
    print(counter, "         ", pounds)
    counter += 1
