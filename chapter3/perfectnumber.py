x = 1
sum_of_factor = 0
number = int(input("Enter a number:  "))
while x < number:
    remainder = number % x
    if remainder == 0:
        sum_of_factor = sum_of_factor + x

        print(x, end=" ")
    x += 1

print()
print("ADDITION OF FACTORS:", sum_of_factor)
if sum_of_factor == number:
    print("PERFECT NUMBER")
if sum_of_factor < number:
    print("DEFICIENT NUMBER")
if sum_of_factor > number:
    print("ADEQUATE NUMBER")
