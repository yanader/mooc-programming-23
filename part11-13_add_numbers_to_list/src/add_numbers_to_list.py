# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers:list):
    if len(numbers) % 5 != 0:
        next_number = max(numbers) + 1
        numbers.append(next_number)
        add_numbers_to_list(numbers)



