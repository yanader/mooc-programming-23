# Copy here code of line function from previous exercise and use it in your solution
def line(x, word):
    lineChar = '*'
    if len(word) != 0:
        lineChar = word[0]
        print(lineChar * x)

def shape(x, c1, y, c2):
    i = 0
    j = 0
    while i < x + 1:
        line(j,c1)
        i+=1
        j+=1
    i = 0
    while i < y:
        line(x,c2)
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")