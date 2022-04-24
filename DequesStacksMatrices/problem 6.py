def up(row, col):
    row,col = row - 1, col
    return row,col


def down(row, col):
    row,col = row + 1, col
    return row,col


def left(row, col):
    row,col = row, col - 1
    return row,col


def right(row, col):
    row,col = row, col + 1
    return row,col

def is_valid(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False

given_string = input()
size = int(input())

matrix = [[x for x in list(input())] for _ in range(size)]

player = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'P':
            player.append((row,col))

current_row, current_col = player[0][0], player[0][1]

commands = int(input())


next_row = int
next_col = int

for _ in range(commands):

    command = input()

    if command == 'up':
        next_row, next_col = up(current_row,current_col)
    elif command == 'down':
        next_row,next_col = down(current_row,current_col)
    elif command == 'left':
        next_row, next_col = left(current_row, current_col)
    elif command == 'right':
        next_row, next_col = right(current_row,current_col)

    if is_valid(next_row,next_col):
        if matrix[next_row][next_col].isalpha():
            given_string += matrix[next_row][next_col]
            matrix[current_row][current_col], matrix[next_row][next_col] = '-', 'P'
        if matrix[next_row][next_col] == '-':
            matrix[current_row][current_col], matrix[next_row][next_col] = '-', 'P'

    else:
        given_string = given_string[:-1]
        continue

    current_row, current_col = next_row,next_col
print(given_string)
for sublist in matrix:
    print(*sublist, sep='')