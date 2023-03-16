# Write your solution here
def double_items(numbers: list):
    return_numbers = []
    for i in range(len(numbers)):
        return_numbers.append(numbers[i] * 2)
    return return_numbers