num = int(input("Enter the length of the triangle: "))
print(num)
for count in range(1, num + 1):
    print("* " * count)

print()
for count in range(1, num + 1):
    if count == 1:
        print("* " * num)
    if count == num:
        print("* " * num)
    else:
        space = " " * ((num * 2) - 3)
        print("*{i}*".format(i=space))

print()
for count in range(1, num + 1):
    t = count - 1
    s = count - 2
    space = " " * ((num - t) * 2)
    space2 = " " * (3 + (4 * s))
    if count == 1:
        print("{i}*{i}".format(i=space))
    else:
        print("{i}*{j}*{i}".format(i=space, j=space2))

for inner in range(num - 1, 0, - 1):
    A = inner - 1
    B = inner - 2
    space3 = " " * ((num - A) * 2)
    space4 = " " * (3 + (4 * B))
    if inner == 1:
        print("{i}*{i}".format(i=space3))
    else:
        print("{i}*{j}*{i}".format(i=space3, j=space4))
