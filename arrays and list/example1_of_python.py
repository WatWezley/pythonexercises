from array import *

x = array("i", [4, 8, 9, 56])
print(len(x))
print(x[2])

sentence = ["Obi is a boy",
            "Ada is a girl",
            "Tommy is a dog"]
print(sentence[0])
print(sentence[1])
print(sentence[0][0:3])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 56, 34, ]
numbers.append("bolaji")
numbers.insert(5,"ugochi")
print(numbers)
print(numbers[0:4])
print(numbers[1:8:2])
print(numbers[-3:-11: -2])

example = "mississippi"
#print(example[0:4],[4:8],[8:11])
