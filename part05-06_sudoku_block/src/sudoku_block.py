# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no + 3):
            numbers.append(sudoku[i][j])
    for n in numbers:
        if numbers.count(n) > 1 and n != 0:
            return False
    return True