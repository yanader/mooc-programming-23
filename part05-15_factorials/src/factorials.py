# Write your solution here
def factorials(n: int):
    dict = {}
    for i in range(1,n+1):
        dict[i] = factorial(i)
    return dict

def factorial(n: int):
    f = 1
    for i in range (1,n+1):
        f*=i
    return f

if __name__ == "__main__":
    print(factorial(5))