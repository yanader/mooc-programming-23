# Write your solution here
def most_common_character(str):
    letter = str[0]
    letterCount = str.count(letter)
    for c in str:
        if str.count(c) > letterCount:
            letterCount = str.count(c)
            letter = c
    return letter