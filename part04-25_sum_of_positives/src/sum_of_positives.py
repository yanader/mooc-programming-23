# Write your solution here
def sum_of_positives(my_list: list):
    result = 0
    for i in my_list:
        if i > 0:
            result += i
    return result