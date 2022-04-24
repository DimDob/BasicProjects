from threading import Thread


def adding(n, letter_c, number_c):
    if n % 2 != 0:
        return Myarray.append(chr(letter_c))
    else:
        return Myarray.append(chr(number_c))

last_index = int(input())


Myarray = []
indexes = []

for x in range(0, last_index+1):
    indexes.append(x)

letter_code = 65
number_code = 48



for i in indexes:
    thread = Thread(target=adding, args=(i, letter_code, number_code))
    thread2 = Thread(target=adding, args=(i, letter_code, number_code))
    if i % 2 == 0:
        thread.start()
        number_code += 1

    else:
        thread2.start()
        letter_code += 1



    if number_code == 57:
        number_code = 48
    if letter_code == 90:
        letter_code = 65


print(Myarray)



