# Write your solution here
def length_of_longest(ls: list):
    longest = 0
    for str in ls:
        if len(str) > longest:
            longest = len(str)
    return longest