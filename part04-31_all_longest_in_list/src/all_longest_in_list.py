# Write your solution here
def all_the_longest(my_list: list):
    return_list = []
    length = 0
    for str in my_list:
        if len(str) > length:
            length = len(str)
    for str in my_list:
        if len(str) == length:
            return_list.append(str)
    return return_list