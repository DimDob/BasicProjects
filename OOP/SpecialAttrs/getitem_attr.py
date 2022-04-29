class MyClass:
    def __init__(self, one: list, two:list):
        self.one = one
        self.two = two


    def get_two(self):
        return self.two

    def __getitem__(self, item):
        if item < 0 or item > len(self.one):
            return 0
        if item == 'one':
            return self.one[item]
        return self.two[item]




    def __setitem__(self, key, value):
        self.one[key] = value
        return self.one[key]

obj_one = MyClass([1, 2, 3], [3,4,5])
x = obj_one.one[4] + obj_one.two[1]
