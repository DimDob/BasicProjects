import concurrent.futures


def adding_letter(param):
    obj.array1.append(param)


def adding_number(n):
    obj.array2.append(n)




class Arrays:
    def __init__(self):
        self.array1 = []
        self.array2 = []

obj = Arrays()


with concurrent.futures.ThreadPoolExecutor() as executor:
        t1 = [executor.submit(adding_letter, chr(i)) for i in range(97, 123)]
        t2 = [executor.submit(adding_number, n) for n in range(48, 57)]

print(obj.array1)
print(obj.array2)

