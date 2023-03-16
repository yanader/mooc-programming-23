# Write your solution here
def shortest(ls: list):
    shortestLength = len(ls[0])
    shortestValue = ls[0]
    for str in ls:
        if len(str) < shortestLength:
            shortestLength = len(str)
            shortestValue = str
    return shortestValue