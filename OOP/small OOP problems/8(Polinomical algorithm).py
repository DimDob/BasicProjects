class Polinomical:
    def __init__(self, arg, data: list):
        self.arg = arg
        self.data = data

    def eval_polynomial(self):
        return sum((current_el*self.arg**idx for idx,current_el in enumerate(self.data)))


    def multiply_by_one_term(self):
        return [0]*self.arg + [self.arg*idx for idx in self.data]

obj = Polinomical(3, [1,2,3])
print(obj.eval_polynomial())
print(obj.multiply_by_one_term())