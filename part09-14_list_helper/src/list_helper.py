# WRITE YOUR SOLUTION HERE:

class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list:list):
        return max(set(my_list), key = my_list.count)

    @classmethod
    def doubles(cls, my_list:list):
        doubles = 0
        for item in set(my_list):
            if my_list.count(item) >= 2:
                doubles += 1
        return doubles
