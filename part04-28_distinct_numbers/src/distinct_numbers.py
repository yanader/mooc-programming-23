# Write your solution here
def distinct_numbers(my_list: list):
    return_list = []
    for i in my_list:
        if return_list.count(i) == 0:
            return_list.append(i)
    return sorted(return_list)