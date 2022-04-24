class MyClass:
    def __init__(self, val):
        if not isinstance(val, list):
            return
        self.val = val

    @property
    def val(self):
        return self.__val

    @val.setter
    def val(self, value: list):

        self.__val = [x for x in value if type(x) == str]

    def __str__(self):
        res = ''
        for el in self.val:
            res += el[0]
        return res

obj = MyClass([1, 2, "Hello", 'i', ' ', "i", "'", 4, 'm', 3, 4, ' ', 'D', 'i', 'm', 4, 'i', 6, 7, 't', 'h', 'e', 'r'])
print(obj)