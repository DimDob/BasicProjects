class MyClass:
    def __init__(self, integer, string_type, is_float):
        self.integer = integer
        self.string_type = string_type
        self.is_float = is_float

    def __int__(self):
        return f'Type of {self.integer} is of class int.'

    def __str__(self):
        return f"Type of '{self.string_type}' is of class str."

    def __float__(self):
        return f"Type of {self.is_float} is of class float."

obj = MyClass(1, 'hello', 5.1)
print(obj.__int__())
print(obj.__str__())
print(obj.__float__())