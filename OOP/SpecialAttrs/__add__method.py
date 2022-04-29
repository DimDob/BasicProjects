class MyClass:
    def __init__(self, vals):
        if not isinstance(vals, list):
            return
        self.vals = vals

    def __add__(self, other):
        return self.vals + other

obj_1 = [1,2,3]
obj_2 = [4,5,6]
print(obj_1.__add__(obj_2))
print(obj_1 + [1,7,5])