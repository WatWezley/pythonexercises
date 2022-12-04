x = "hello boss baby"

for i, l in enumerate(x, start=1):
    if l != "b":
        print(f"{l}", end="")
print()

for i, l in enumerate(x, start=1):
    if l == "b":
        print(f"{l}----->{i}")
print()

for i in x:
    if i == "b":
        print(i)

for i in x:
    if i != "b":
        print(i, end="")
print()

for i in range(len(x)):
    if x[i] == "b":
        print(x[i], ":", i)

print()

for i in range(len(x)):
    if x[i] != "b":
        print(x[i], ":", i)
