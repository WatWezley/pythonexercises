
x = 1
factor = 0
num = int(input("Enter a number:  "))
while x <= num:
    remainder = num % x
    if remainder == 0:
        factor = factor+1
        print(x, end=" ")
    x += 1

print()
print("the number of factors of factors", "is", factor)
if factor == 2:
    print("This is a prime number")
else:
    print("This is not a prime number")


