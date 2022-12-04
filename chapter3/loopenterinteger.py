
count = 2
largest_so_far = 23
while count < 5:
    num = int(input("Give me a number: "))
    if num > largest_so_far:
        largest_so_far = num

    count += 1

print("The largest number is", largest_so_far)