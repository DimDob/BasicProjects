from collections import defaultdict


class FullColumn(Exception):
    pass


def valid_column(column):
    if not 0 <= column < cols:
        raise IndexError


def filling_matrix(current_column, current_matrix_rows):
    row = current_matrix_rows
    col = current_column
    try:
        if matrix[row][col] != 0:
            while matrix[row][col] != 0:
                row -= 1
            matrix[row][col] = current_player

        else:
            matrix[row][col] = current_player

    except IndexError:
        return
    except TypeError:
        return

    return row, col


def horizontal(row, col):
    result = []
    for el in range(cols):
        if matrix[row][el] == current_player:
            result.append(True)

        else:
            result.append(False)
    if all(result[:cols - 3]) or all(result[1:cols - 2]) or all(result[2:cols - 1]) or all(
            result[3:cols]):  # TODO must subtract by 1 if size is changed.
        return True


def vertical(row, col):
    result = []
    last_row = rows - 1
    for el in range(rows - 1, -1, -1):
        if matrix[el][col] == current_player:
            result.append(True)
        else:
            result.append(False)
    if all(result[rows - 4:rows]) or all(result[rows - 5:rows - 1]) or all(
            result[rows - 6:rows - 2]):  # TODO must subtract by 1 if size is changed.
        return True


def full_column(current_col):
    current_elements = []
    for el in range(current_col):
        current_elements.append(el)
    for el in current_elements:
        if not any(current_elements):
            return FullColumn


def diagonal(row, col):
    diagonal1 = defaultdict(list)  # For the top right to bottom left
    diagonal2 = defaultdict(list)  # For the top left to bottom right
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            diagonal1[i - j].append(matrix[i][j])
            diagonal2[i + j].append(matrix[i][j])

    for key, value in diagonal1.items():
        if len(value) >= 4:
            if value.count(1) == 4 or value.count(2) == 4:
                return True
    for key, value in diagonal2.items():
        if len(value) >= 4:
            if value.count(1) == 4 or value.count(2) == 4:
                return True


def is_winner(row, col):
    if horizontal(row, col) or vertical(row, col) or diagonal(row, col):
        return True
    else:
        return False


rows = 6
cols = 7

matrix = [[0 for _ in range(cols)] for _ in range(rows)]
current_player = 1

while True:
    current_player = 2 if current_player % 2 == 0 else 1

    try:
        current_column = int(input(f"Player {current_player}, please choose a column: ")) - 1
        valid_column(current_column)
        next_row, next_col = filling_matrix(current_column, rows - 1)  # Determination of next row/col indexes
        matrix[next_row][
            next_col] = current_player  # If they are valid the current row/col are interpreted as the new position of the player
        if is_winner(next_row, next_col):  # checking if there are 4 same types of indexes
            print(*matrix, sep='\n')
            print(f"Winner is player {current_player}.")
            break

        print(*matrix, sep='\n')



    except (FullColumn, TypeError):
        print(f'This column is full. Player {current_player} please enter a valid one.')


    except IndexError:
        print(f"This input is outside the table. Please enter an valid integer.")
        continue

    except ValueError:
        print(f'Invalid input. Player {current_player} please select an integer')
        continue

    current_player += 1