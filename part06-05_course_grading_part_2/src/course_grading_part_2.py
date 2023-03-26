# write your solution here
def create_student_dict(s: str):
    student_dictionary = {}
    with open(s) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            student_dictionary[parts[0]] = parts[1].strip() + ' ' + parts[2].strip()
    return student_dictionary

def create_exercises_dict(s: str):
    exercises_dictionary = {}
    with open(s) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            count = 0
            for i in parts[1:]:
                i = i.strip()
                i = int(i)
                count += i
            exercises_dictionary[parts[0]] = count
    return exercises_dictionary

def create_exam_points(s: str):
    exam_points_dictionary = {}
    with open(s) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            sum = 0
            for i in parts[1:]:
                i = i.strip()
                i = int(i)
                sum += i
            exam_points_dictionary[parts[0]] = sum
    return exam_points_dictionary

def combined_name_and_exercises(stu_dict: dict, exer_dict: dict):
    for id, name in stu_dict.items():
        if id in exer_dict:
            exercise_count = exer_dict[id]
            print(f'{name} {exercise_count}')

def combined_name_and_points(stu_dict: dict, points_dict: dict):
    for id, name in stu_dict.items():
        if id in points_dict:
            points = points_dict[id]
            print(f'{name} {points}')

def print_grades(stu_dict: dict,exer_dict: dict, points_dict: dict):
    grade_dict = {}
    for id, name in stu_dict.items():
        exercise_points = exer_dict[id] // 4
        total_points = exercise_points + points_dict[id]
        if total_points < 15:
            grade = 0
        elif total_points < 18:
            grade = 1
        elif total_points < 21:
            grade = 2
        elif total_points < 24:
            grade = 3
        elif total_points < 28:
            grade = 4
        else:
            grade = 5
        print(f'{name} {grade}')


file1 = input("Student information: ")
file2 = input("Exercises information: ")
file3 = input("Exam points: ")

#file1 = 'students1.csv'
#file2 = 'exercises1.csv'
#file3 = 'exam_points1.csv'

student_dict = create_student_dict(file1)
exercises_dict = create_exercises_dict(file2)
points_dict = create_exam_points(file3)

#print('Exercises:')
#combined_name_and_exercises(student_dict, exercises_dict)
#print('Points:')
#combined_name_and_points(student_dict, points_dict)
print_grades(student_dict, exercises_dict, points_dict)
