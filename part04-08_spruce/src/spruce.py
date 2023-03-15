# Write your solution here
def spruce(x):
    print('a spruce!')
    i = 0
    while i < x:
        print(' '*(x-i-1),end='')
        print('*'*((i*2)+1))
        i+=1
    print(' '*(x-1),end='')
    print('*')
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)