# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for row in sudoku:
        new_row = []
        new_row[:] = row
        sudoku_copy.append(new_row)
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

def print_sudoku(sudoku: list):
    i = 1
    j = 1
    for row in sudoku:
        for element in row:
            if element == 0:
                print('_ ',end='')
                if i % 3 == 0:
                    print(' ',end='')
                i+=1
            else:
                print(str(element) + ' ',end='')
                if i % 3 == 0:
                    print(' ',end='')
                i+=1
        print()
        if j % 3 == 0:
            print()
        j+=1

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)