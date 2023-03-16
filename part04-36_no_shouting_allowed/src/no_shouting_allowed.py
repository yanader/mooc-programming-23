# Write your solution here
def no_shouting(ls: list):
    return_list = []
    for str in ls:
        if not str.isupper():
            return_list.append(str)
    return return_list