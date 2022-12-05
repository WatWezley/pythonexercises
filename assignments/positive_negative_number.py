number = int(input("Enter a number,the input ends if number is 0: "))
counter = 1
positive_numbers = 0
negative_numbers = 0
sum_of_integer = 0
while number != 0:
    if number > 0:
        positive_numbers = positive_numbers + 1
    else:
        negative_numbers = negative_numbers + 1
    sum_of_integer = sum_of_integer + number
    number = int(input("Enter a number,the input ends if number is 0: "))
    counter += 1
average = sum_of_integer // counter
print("The positive numbers are :", positive_numbers)
print("The negative numbers are :", negative_numbers)
print("The sum is :", sum_of_integer)
print("The average is :", average)
