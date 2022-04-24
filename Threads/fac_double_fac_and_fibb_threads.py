import concurrent.futures
import math
from time import sleep


def factorial(n):
    return math.factorial(n)



def double_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * double_factorial(n - 2)


def fibb(end):
    array = [1,1,2]
    a = array[-2]
    b = array[-1]

    for i in range(2, end+1):
        a, b = b, a+b
        array.append(b)

    return array



fac_num = int(input())
double_fac_num = int(input())
fib_num = int(input())


with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = [executor.submit(factorial, fac_num)]
    t2 = [executor.submit(double_factorial, double_fac_num)]
    t3 = [executor.submit(fibb, fib_num)]

    for t in concurrent.futures.as_completed(t1):
        print(f"Factorial of {fac_num}: {t.result()}")
        sleep(2)

    for t in concurrent.futures.as_completed(t2):
        print(f"Double factorial of {double_fac_num}: {t.result()}")
        sleep(2)

    for t in concurrent.futures.as_completed(t3):
        print(f"Fibonacci of {fib_num}: {t.result()}")
