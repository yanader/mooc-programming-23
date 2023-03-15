# Write your solution here
def line(x, word):
    lineChar = '*'
    if len(word) != 0:
        lineChar = word[0]
        print(lineChar * x)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")