size = 6

matrix = [[x for x in input().split()] for _ in range(size)]


bucket_positions = []

for row in range(size):
    for col in range(size):
        if matrix[row][col].isnumeric():
            matrix[row][col] = int(matrix[row][col])
        else:
            bucket_positions.append((row,col))



total_points_collected = 0

def hit(row,col):
    current_result = 0
    if 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == 'B' and (row,col) in bucket_positions:
            bucket_positions.remove((row,col))
            for x in range(size):
                if type(matrix[x][col]) == int:
                    current_result += matrix[x][col]


        else:
            return current_result
    return current_result

def price_won(total_collected_points):
    price = ''
    if 100 <= total_collected_points <= 199:
        price = 'Football'
    elif 200 <= total_collected_points <= 299:
        price = 'Teddy Bear'
    elif total_collected_points >= 300:
        price = 'Lego Construction Set'
    return price





for _ in range(3):
    hit_coordinates = input().split(', ')
    current_row = int(hit_coordinates[0][1:])
    current_col = int(hit_coordinates[1][:-1])
    total_points_collected += hit(current_row, current_col)

if not price_won(total_points_collected) == '':
    print(f"Good job! You scored {total_points_collected} points, and you've won {price_won(total_points_collected)}.")
else:
    print(f"Sorry! You need {100 - total_points_collected} points more to win a prize.")
