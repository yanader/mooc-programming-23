# Write your solution here
def formatted(my_list: list):
    return_list = []
    for i in my_list:
        return_list.append(f'{i:.2f}')
    return return_list