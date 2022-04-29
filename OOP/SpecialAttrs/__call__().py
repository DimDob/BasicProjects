class Alpha:
    def __call__(self, n):
        s = 0
        for k in range(len(self.nums)):
            s += self.nums[k] ** n
        return s


class Bravo:
    def __call__(self, x, y): #Чрез извикване на __call__() се извиква обектът
        # self.num = 3
        # self.val = 2 # В случая мат.операция е '+' и можем да придадем стойности на полетата self.num/self.val и във вътешния scope на метода (в този случай, ако има дефинирани и извън този скоуп, ще се вземат тези, които са в метода)
        return self.num * x + self.val*y


# Методът __call__() е специален механизъм, чрез който се дава възможност обект да бъде извикан като функция: след името на обекта в кръгли скоби може да се укаже аргумент и такъв израз да върне резултат.
class Alpha_2:
    def __call__(self, n):
        k = 0
        for _ in range(len(self.nums)):
            k += 2
        return k

A = Alpha_2()
A.nums = [1,2,3,4,5]
print(A(A.nums))

A = Alpha()
A.nums = [1,2,3]
print("A(1) =", A(1))
print(f"A(2) =", A(2))
B = Bravo()
B.num = 2
B.val = 3
print("B(5,1) =", B(5,1))
print("B(3,4) =", B(3,4))