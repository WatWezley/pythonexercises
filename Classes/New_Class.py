class New_Class:

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_age(self, age: int):
        self.age = age

    def get_age(self):
        return self.age


ugo = New_Class("favour", 30)
print(ugo.first_name)



