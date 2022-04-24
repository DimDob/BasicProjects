class Odd:
    def __init__(self, n):
        self.n = n
        self.iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.iteration <= self.n:
            current_number = self.iteration
            self.iteration += 1
            if not current_number % 2 == 0:
                return current_number
        else:
            raise StopIteration


obj = Odd(5)
print(list(obj))