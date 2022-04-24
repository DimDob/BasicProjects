import concurrent.futures
import string


def adding(n, i):
    try:
        if i == 0:
            return arr[0].append(n)
        arr[1].append(n)
    except IndexError:
        raise IndexError('Index out of range.')

arr= [[] for _ in range(int(input()))]
end = int(input())



with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = [executor.submit(adding, n, 0) for n in range(end)]
    t2 = [executor.submit(adding, n, 1) for n in string.ascii_lowercase]

print(arr)