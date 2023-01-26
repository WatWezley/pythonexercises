value = dict(name="mr ugo", age="30")
print(value)

value = {
    "Name": "favour",
    "Age": 30,
    "Skill": {
        "Soft": ["Washing plate", "communication"

                 ],
        "Tech": ["Full Stack", "Middle End", "Back End"

                 ]}
}
print(value["Name"])
print(value["Skill"]["Tech"][2])

# how to add into a dictionary
value["age"] = 45
value.update({"Name": 56})

# how to add to a list in a dictionary
val = value["Skill"]["Tech"]
val.append("Front End")
print(value)
