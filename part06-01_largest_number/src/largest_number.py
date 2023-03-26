# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for line in new_file:
            if int(line) > largest:
                largest = int(line)
    return largest

if __name__ == "__main__":
    print(largest())