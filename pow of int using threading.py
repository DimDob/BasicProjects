import math


class Undefined(Exception):
    pass


class InvalidDivide(Exception):
    pass



while True:

    try:

        A = int(input())
        x = int(input())
        B = int(input())

        result = (math.pow(A, 2) - 1)

        if x == 0 or result == 0:
            raise InvalidDivide
        if B == 0:
            raise Undefined

        B = result * x

        result_array = [
            f'B = (math.pow(A, 2) - 1)*x',
            f'{B} = {result}*x',
            f'x = {B / result}',
        ]

        for res in result_array:
            print(f'{res}')

    except InvalidDivide:
        print('Cannot divide by zero.')

    except Undefined:
        print('Undefined')

    except ValueError:
        print('Please enter a valid integer.')