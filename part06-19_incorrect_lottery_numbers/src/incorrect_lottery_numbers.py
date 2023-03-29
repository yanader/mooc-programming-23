def is_week_valid(week: str):
    try:
        week = int(week)
        print(week + 1)
        return True
    except:
        return False
def are_numbers_valid(numbers: str):
    try:
        numbers_list = numbers.split(',')
        if len(numbers_list) != 7:
            return False
        for num in numbers_list:
            number = int(num)
            if number < 1 or number > 39 or numbers_list.count(num) != 1:
                return False
        return True
    except:
        return False

def filter_incorrect():
    open('correct_numbers.csv', 'w').close()
    correct_file = open('correct_numbers.csv', 'a')
    with open('lottery_numbers.csv') as lottery_file:
        for line in lottery_file:
            line = line.replace('\n','')
            parts = line.split(';')
            week = parts[0].split(' ')[1]
            numbers = parts[1]
            if is_week_valid(week) and are_numbers_valid(numbers):
                correct_file.write(line + '\n')
    correct_file.close()

if __name__ == "__main__":
    #filter_incorrect()
    print(are_numbers_valid('21,2,22,14,4,28,38'))
   