# Write your solution here
def even_numbers(my_list:list):
    return_list = []
    for i in my_list:
        if i % 2 == 0:
            return_list.append(i)
    return return_list