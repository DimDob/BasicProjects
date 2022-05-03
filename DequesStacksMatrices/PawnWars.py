import sys

def white_up(row, col):
    row, col = row - 1, col
    return row, col


def black_up(row, col):
    row, col = row + 1, col
    return row, col


def is_valid(row, col):
    if 0 < row < size - 1:
        return True
    return False


def white_diagonal_left(row, col):  # left diag
    if 0 <= row - 1 < size and 0 <= col - 1 < size:

        if matrix[row - 1][col - 1] == 'b':
            matrix[row][col] = '-'
            matrix[row - 1][col - 1] = 'w'
            return True
    return False


def white_diagonal_right(row, col):
    if 0 <= row - 1 < size and 0 <= col + 1 < size:
        if matrix[row - 1][col + 1] == 'b':
            matrix[row][col] = '-'
            matrix[row - 1][col + 1] = 'w'
            return True
    return False


def black_diagonal_left(row, col):
    if 0 <= row + 1 < size and 0 <= col - 1 < size:
        if matrix[row + 1][col - 1] == 'w':
            matrix[row][col] = '-'
            matrix[row + 1][col - 1] = 'b'
            return True
    return False


def black_diagonal_right(row, col):
    if 0 <= row + 1 < size and 0 <= col + 1 < size:
        if matrix[row + 1][col + 1] == 'w':
            matrix[row][col] = '-'
            matrix[row + 1][col + 1] = 'b'
            return True
    return False


size = 8

matrix = [[x for x in input().split()] for _ in range(size)]
black = []
white = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'b':
            black.append((row,col))
        elif matrix[row][col] == 'w':
            white.append((row,col))
chess_board = {}
current_col = 8
# for z in range(size):
#     letter = 'a'
#
#     for y in range(size):
#         chess_board[f"{letter}{current_col}"] = (z,y)
#         letter =chr(ord(letter) + 1)
#     current_col -= 1

for z in range(size):
    letter = 'a'
    for y in range(size):
        chess_board[(z,y)] = f"{letter}{current_col}"
        letter = chr(ord(letter) + 1)
    current_col -= 1
white_row, white_col = white[0][0], white[0][1]
black_row, black_col = black[0][0], black[0][1]
while True:

    next_white_row, next_white_col= white_up(white_row, white_col)
    next_black_row, next_black_col = black_up(black_row, black_col)

    if is_valid(next_white_row, next_white_col):
        if white_diagonal_left(white_row, white_col) or white_diagonal_right(white_row, white_col):
            print(f"Game over! White win, capture on {chess_board[black_row, black_col]}.")
            sys.exit()
        else:
            matrix[white_row][white_col] = '-'
            white_row,white_col = next_white_row, next_white_col
            matrix[white_row][white_col] = 'w'
    else:
        print(f"Game over! White pawn is promoted to a queen at {chess_board[next_white_row,next_white_col]}.")
        sys.exit()

    if is_valid(next_black_row, next_black_col):
        if black_diagonal_left(black_row,black_col) or black_diagonal_right(black_row, black_col):
            print(f"Game over! Black win, capture on {chess_board[white_row, white_col]}.")
            sys.exit()
        else:
            matrix[black_row][black_col] = '-'
            black_row, black_col = next_black_row, next_black_col
            matrix[black_row][black_col] = 'b'
    else:
        print(f"Game over! Black pawn is promoted to a queen at {chess_board[next_black_row, next_black_col]}.")