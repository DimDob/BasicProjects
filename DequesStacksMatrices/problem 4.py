import math


def valid_command(command_input):
    if command_input == 'up' or command_input == 'down' or command_input == 'left' or command_input == 'right':
        return True
    return False

def movement(row, col, current_input):

    if current_input == "up":
        if 0 <= row -1 < size:
            row = row-1
        else:
            if row - 1 == -1:
                row = size - 1
    elif current_input == 'down':
        if 0 <= row + 1 < size:
            row += 1
        else:
            row = 0
    elif current_input == 'left':
        if 0 <= col - 1 < size:
            col -= 1
        else:
            col = size - 1
    elif current_input == 'right':
        if 0 <= col + 1 < size:
            col += 1
        else:
            col = 0

    return row,col


size = int(input())

matrix = [[x for x in input().split()] for _ in range(size)]

player_position = []
walls_positions = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'P':
            player_position.append((row,col))
        elif matrix[row][col].isnumeric():
            matrix[row][col] = int(matrix[row][col])

        elif matrix[row][col] == 'X':
            walls_positions.append((row,col))

total_collected_coins = 0
win = False
current_row = player_position[0][0]
current_col = player_position[0][1]

path_taken = [(current_row,current_col)]


while True:
    if total_collected_coins >= 100:
        win = True
        break
    command = input()
    if valid_command(command):
        next_row, next_col = movement(current_row, current_col, command)
        path_taken.append((next_row, next_col))
        if (next_row,next_col) in walls_positions:
            total_collected_coins = math.floor(total_collected_coins/2)
            break
        else:
            if path_taken.count((next_row,next_col)) == 1:
                if type(matrix[next_row][next_col]) == int:
                    current_coins = matrix[next_row][next_col]
                    total_collected_coins += current_coins
                    matrix[current_row][current_col] = matrix[next_row][next_col]
                    matrix[next_row][next_col] = 'P'
                    current_row,current_col = next_row,next_col
            else:
                if matrix[next_row][next_col] != 'X':
                    matrix[current_row][current_col] = matrix[next_row][next_col]
                    matrix[next_row][next_col] = 'P'
                    current_row, current_col = next_row, next_col
                else:
                    break

    else:
        pass

if win:
    print(f"You won! You've collected {math.floor(total_collected_coins)} coins.")
else:
    print(f"Game over! You've collected {math.floor(total_collected_coins)} coins.")


print(f"Your path:")
for item in path_taken:
    print(list(item))


