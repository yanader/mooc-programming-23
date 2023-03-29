# Write your solution here
def filter_solutions():
    correct_string = ''
    incorrect_string = ''
    with open('solutions.csv') as new_file:
        for line in new_file:
            parts = line.replace('\n','').split(';')
            if '+' in parts[1]:
                addition_parts = parts[1].split('+')
                if int(addition_parts[0]) + int(addition_parts[1]) == int(parts[2]):
                    correct_string += line + '\n'
                else:
                    incorrect_string += line + '\n'
            else:
                subtraction_parts = parts[1].split('-')
                if int(subtraction_parts[0]) - int(subtraction_parts[1]) == int(parts[2]):
                    correct_string += line + '\n'
                else:
                    incorrect_string += line + '\n'
    new_file.close()
    with open('correct.csv','w') as correct_file:
        correct_file.write(correct_string)
        correct_file.close()
    with open('incorrect.csv','w') as incorrect_file:
        incorrect_file.write(incorrect_string)
        incorrect_file.close()