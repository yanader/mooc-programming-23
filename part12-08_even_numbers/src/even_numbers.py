# Write your solution here
def even_numbers(beginning:int, maximum:int):
    if beginning % 2 == 0:
        i = beginning
    else:
        i = beginning + 1
    while i <= maximum:
        yield i
        i +=2


