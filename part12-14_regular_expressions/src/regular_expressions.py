# Write your solution here
import re

def is_dotw(my_string: str):
    expression = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun'
    if re.search(expression, my_string):
        return True
    else:
        return False

def all_vowels(my_string:str):
    expression = '^[aeiou]+$'
    if re.search(expression, my_string):
        return True
    else:
        return False

def time_of_day(my_string:str):
    expression = '([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]'
    if re.search(expression, my_string):
        return True
    else:
        return False


# while True:
#     input_string = input("Enter a string: ")
#     if input_string == "":
#         break
#     print(all_vowels(input_string))