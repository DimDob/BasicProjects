class MyError(Exception):
    def __init__(self):
        self.values = []

    def __add__(self, value):
        self.values.append(value)
        return self


class InvalidAsciiCode(Exception):
    pass



def error_generator(ascii_val):
    try:
        if ascii_val == 65:
            raise MyError
        elif ascii_val < 65:
            raise InvalidAsciiCode
        error_generator(ascii_val - 1)
    except MyError as error:
        raise error + ascii_val
    except InvalidAsciiCode:
        print('Ascii Code equals no letter.')

def getList(n):
    try:
        error_generator(n)
    except MyError as error:
        return convert_to_chr(error.values)


def convert_to_chr(codes):
    res = [chr(code) for code in codes]
    return res[::-1]

A = getList(90) #'Z' ascii code is 90
print(A)
B = getList(65)
print(B)
C =getList(54)
