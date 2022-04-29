import statistics


class MyClass():
    def __init__(self, arg_list):
        arg_list = [x for x in arg_list if x.isnumeric()]
        self.arg_list = arg_list
        self.arg_list = [int(x) for x in self.arg_list]

    def show(self):
        return print(f'The argument list: {self.arg_list}')

    def average(self):
        return print(f'Average value in args list is: {statistics.mean(self.arg_list):.2f}')


current_list = [x for x in input().split()]
obj = MyClass(current_list)
obj.show()
obj.average()