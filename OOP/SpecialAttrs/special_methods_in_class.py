class MyClass:
    def __init__(self, values):
        if not isinstance(values, list):
            return
        self.values = values

    def __len__(self, other):
        diff = abs(len(self.values) - len(other.values))
        if len(self.values) < len(other.values):
            for _ in range(diff):
                self.values.append(0)
            return self.values
        for _ in range(diff):
            other.values.append(0)
        return other.values

    def __eq__(self, other):
        return self.values[0] == other.values[0]

    def __ne__(self, other):
        return bool(self.values[1] != other.values[1])

    def __lt__(self, other):
        return bool(self.values[2] < other.values[2])

    def __gt__(self, other):
        return bool(self.values[3] > other.values[3])

    def __ge__(self, other):
        return bool(self.values[4] >= other.values[4])

    def __le__(self, other):
        return bool(self.values[5] <= other.values[5])



obj_1 = MyClass([1,2,3,4])
obj_2 = MyClass([1,6,7,8, 3, 7])
obj_1.__len__(obj_2)
print(obj_1 == obj_2)
print(obj_1 != obj_2)
print(obj_1 < obj_2)
print(obj_1 > obj_2)
print(obj_1 >= obj_2)
print(obj_1 <= obj_2)