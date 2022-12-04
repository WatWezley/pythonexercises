hello = "Hello there!!!"
print(hello.find("e"))

print(hello.upper())
print(hello.lower())
print(hello.title())
print(hello.capitalize())
print(hello.casefold())
print(hello.swapcase())

print(hello.lower().count("e"))
print(hello.center(20))
print(hello.center(20, "*"))
print(hello.ljust(20, "*"))
print(hello.rjust(20, "x"))


for i in range (1,21,2):
    asterisk = "*" * i
    print(asterisk.center(20))

print(hello.endswith("!!!"))
print(hello.startswith("h"))
print(hello.isalpha())

print(hello.replace("l", "q"))
print(hello.replace("l", "q", 1))
print("-".join(["a", "b", "c"]))

bin_ = "10101101110111"
print(bin_.replace("1", "X").replace("0", "1").replace("X", "0"))
print(bin_.translate(str.maketrans("01","01")))


