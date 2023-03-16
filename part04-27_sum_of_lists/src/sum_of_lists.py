# Write your solution here
def list_sum(list1: list, list2: list):
    return_list = []
    i = 0
    while i < len(list1):
        return_list.append(list1[i] + list2[i])
        i+=1
    return return_list