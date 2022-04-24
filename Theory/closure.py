def func():
    i = 0

    def add(): #closure
        nonlocal i
        i += 1

    def sub():
        return i

    return add, sub


add, get = func()
add()
add()
add()
add()
print(get())



