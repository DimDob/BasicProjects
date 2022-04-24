import concurrent.futures
# import time
# from threading import Thread, Event
from time import sleep

stop = int(input())
integers = []

for x in range(0, stop+1):
    integers.append(x)


def calc_pow_of_int(n):
    return f"{n} to the power of 2: {pow(n, 2)}"

#
# threads = [Thread(target=calc_pow_of_int, args=[x]) for x in integers]
#
# myevent = Event()
# for t in threads:
#     myevent.set()  # raising a flag so we could sync them.
#     t.start()
#     sleep(3)
#     myevent.clear()
#
#
# for t in threads:
#     if t.is_alive():
#         t.join()

with concurrent.futures.ThreadPoolExecutor() as executor: #creates an obj of the current class

    results = [executor.submit(calc_pow_of_int, integer) for integer in integers]
    for f in concurrent.futures.as_completed(results): #creates a generator with results in results var
        print("Calculating...")
        sleep(2)
        print(f.result())
        sleep(1)
