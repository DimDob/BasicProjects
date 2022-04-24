class MyClass:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __rsub__(self, other):
        return abs(self.number - other)

    def __mul__(self, other):
        return self.number * other

    def __truediv__(self, other):
        return self.number / other

obj = MyClass(5)
print(obj + 5)
print(obj - 4)
print(8 - obj)
print(obj * 5)
print(obj / 2)

