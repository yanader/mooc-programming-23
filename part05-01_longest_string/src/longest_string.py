# Write your solution here
def longest(strings: list):
    length = 0
    longest = ''
    for s in strings:
        if len(s) > length:
            length = len(s)
            longest = s
    return longest