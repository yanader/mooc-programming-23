# Copy here code of line function from previous exercise
def line(x, word):
    lineChar = '*'
    if len(word) != 0:
        lineChar = word[0]
        print(lineChar * x)


def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    j = 1
    while i < size:
        line(j, "#")
        i+=1
        j+=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
