# Write your solution here
def transpose(matrix: list):
    matrix_copy = []
    for row in matrix:
        matrix_copy.append(row[:])
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix_copy[j][i]

if __name__ == "__main__":
    board = [["1", "2"], ["1", "2"]]
    print(board)
    transpose(board)
    print(board)