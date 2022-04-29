class MyClass():
    def __init__(self, el_one, el_two):
        self.el_one = el_one
        self.el_two = el_two

    def show(self):
        if type(self.el_one) == str and type(self.el_one) == type(self.el_two):
            return self.el_one + self.el_two
        elif type(self.el_one) == int and type(self.el_one) == type(self.el_two):
            return self.el_one + self.el_two


obj = MyClass(1, 2)
print(obj.show())

obj_2 = MyClass('Hello ', 'World!')
print(obj_2.show())