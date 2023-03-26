# write your solution here
def matrix_sum():
    ls = row_sums()
    sum = 0
    for i in ls:
        sum += i
    return sum

def matrix_max():
    max = 0
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.replace('\n','')
            parts = line.split(',')
            for i in parts:
                if int(i) > max:
                    max = int(i)
    return max

def row_sums():
    sumList = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            sum = 0
            line = line.replace('\n','')
            parts = line.split(',')
            for i in parts:
                sum += int(i)
            sumList.append(sum)
    return sumList

if __name__ == "__main__":
    print(matrix_sum())
