"""54. Spiral Matrix"""
"""TC: O(M*N)"""
"""SC: O(M*N)"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def spiral_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, 0
    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
    left_bound, right_bound, up_bound, down_bound = -1, cols, 0, rows
    direction = RIGHT
    result = []

    while len(result) != rows * cols:
        if direction == RIGHT:
            while j != right_bound:
                result.append(matrix[i][j])
                j += 1
            i, j = i + 1, j - 1
            right_bound -= 1
            direction = DOWN
        elif direction == DOWN:
            while i != down_bound:
                result.append(matrix[i][j])
                i += 1
            i, j = i - 1, j - 1
            down_bound -= 1
            direction = LEFT
        elif direction == LEFT:
            while j != left_bound:
                result.append(matrix[i][j])
                j -= 1
            i, j = i - 1, j + 1
            left_bound += 1
            direction = UP
        else:  # direction == UP
            while i != up_bound:
                result.append(matrix[i][j])
                i -= 1
            i, j = i + 1, j + 1
            up_bound += 1
            direction = RIGHT

    return result

print(spiral_matrix(matrix))