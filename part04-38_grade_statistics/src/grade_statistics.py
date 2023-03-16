def user_inputs():
    user_inputs = []
    while True:
        entry = input('Exam points and exercises completed:')
        if entry == '':
            break
        user_inputs.append(entry)
    return user_inputs

def convert_to_grade(str1: str, str2: str):
    score = int(str2) // 10 + int(str1)
    if int(str1) < 10:
        return 0
    elif score >= 28:
        return 5
    elif score >= 24:
        return 4
    elif score >= 21:
        return 3
    elif score >= 18:
        return 2
    elif score >= 15:
        return 1
    else:
        return 0
    
def produce_grade_list(ls: list):
    grade_list = []
    for entry in ls:
        data_points = entry.split(' ')
        grade = convert_to_grade(data_points[0], data_points[1])
        grade_list.append(grade)
    return grade_list

def produce_points_average(ls: list):
    points = []
    for entry in ls:
        data_points = entry.split(' ')
        points.append(int(data_points[0]) + int(data_points[1]) // 10)
    return sum(points)/len(points)

def pass_percentage(ls: list):
    passes = 0
    for i in ls:
        if i > 0:
            passes +=1
    return passes/len(ls)

def produce_statistics(ls: list):
    print('Statistics:')
    average = produce_points_average(ls)
    grades = produce_grade_list(ls)
    pass_rate = pass_percentage(grades) * 100
    print(f'Points average: {average}')
    print(f'Pass percentage: {pass_rate:.1f}')
    print('Grade distribution:')
    return_string = ''
    for i in range(5,-1,-1):
        count = 0
        for j in grades:
            if j == i:
                count +=1
        print(f'  {i}: ' + '*'*count)

def main():
    myList = user_inputs()
    produce_statistics(myList)

main()

