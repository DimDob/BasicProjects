
class Alpha:
    def __init__(self, *args):
        L = []
        for val in args:
            if isinstance(val, int):
                L.append(val)
        self.nums = L

    def __iter__(self): #методът се извиква при извикване на функция iter():
        return Bravo(self.nums) #Създава се обект на класа Bravo посредством класа Аlpha. Като аргумент на конструктора при създаването на този обект се предава референция към списъка, записан в полето nums.


class Bravo:
    def __init__(self, nums):
        L = []
        for n in nums:
            if 10 > n > 0:
                L.append(n)
        self.digits = L
        self.position = - 1

    def __next__(self): #Методът се извиква при извикване на функция next():
        self.position += 1
        if self.position < len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
A = Alpha(2, 'A', 12, 7, -3, 'Hello', 9, 5, 'Alpha')
B = iter(A)

try:
    while True:
        print(next(B), end=' ')
except StopIteration:
    print()
#Клас Браво не е пълноценен итератор, поради факта, че в него няма описан метод __iter__(). Но това може да се поправи, като давата класа се слеят в едно:

class MyClass:
    def __init__(self, *args):
        L = []
        for val in args:
            if isinstance(val, int):
                if 10 > val > 0:
                    L.append(val)
        self.digits = L
        self.position = - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position < len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration

A = MyClass(2, 'A', 12, 7, -3, 'Hello', 9, 5, 'Alpha')
try:
    print('Чрез обединяване: ')
    while True:
        print(next(A), end=' ')
except StopIteration:
    print()


B = MyClass(5, 'B', 1.2, 11, -1, 'Hi', 8, 4, 'Bravo', 3)
for s in B:
    print(s, end=' ')
print()
#Или чрез множествено наследяване, тъй като специалният метод __iter__() е описан в клас Алфа, а __next__() - в Браво, то чрез множествено наследяване
#производният клас наслядява методите на базовия.


class Class_inheritance(Alpha, Bravo):
    pass

A = MyClass(2, 'A', 12, 7, -3, 'Hello', 9, 5, 'Alpha')

try:
    print('Чрез наследяване:')
    while True:
        print(next(A), end=' ')
except StopIteration:
    print()