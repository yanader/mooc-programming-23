# Write your solution here
def row_correct(sudoku: list, row_no: int):
    for i in sudoku[row_no]:
        if i != 0 and sudoku[row_no].count(i) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    for i in column:
        if column.count(i) > 1 and i != 0:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no + 3):
            numbers.append(sudoku[i][j])
    for n in numbers:
        if numbers.count(n) > 1 and n != 0:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0,len(sudoku)):
        if row_correct(sudoku, i):
             continue
        else:
             return False
    for j in range(0,len(sudoku)):
        if column_correct(sudoku, j):
            continue
        else:
            return False
    blocks = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    for block in blocks:
        if block_correct(sudoku,block[0],block[1]):
            continue
        else:
            return False
    return True