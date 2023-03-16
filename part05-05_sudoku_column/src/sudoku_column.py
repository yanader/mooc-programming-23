# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    for i in column:
        if column.count(i) > 1 and i != 0:
            return False
    return True