class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.sequence = [1, 1]
        self.iterations = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.n:
            print(self.sequence)
            raise StopIteration

        a = self.sequence[-2]
        b = self.sequence[-1]

        a, b = b, a+b
        self.sequence.append(b)

        self.iterations += 1


obj = list(Fibonacci(10))
