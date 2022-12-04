x = 1
while x <= 100:
    if x % 15 == 0:
        print("FIZZBUZZ")
    elif x % 3 == 0:
        print("FIZZ")
    elif x % 5 == 0:
        print("BUZZ")
    else:
        print(x)
    x += 1
