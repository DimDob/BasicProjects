
MyArray = []
while True:
    try:
        start = int(input())
        end = int(input())

        for el in range(start, end + 1):
            MyArray.append(el)

        break
    except ValueError:
        print('Invalid data input. Please enter an integer.')
MyArray = ', '.join(map(str, MyArray))
print(MyArray)