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

def combined_output(stu_dict: dict, exer_dict: dict):
    for id, name in stu_dict.items():
        if id in exer_dict:
            exercise_count = exer_dict[id]
            print(f'{name} {exercise_count}')
            


file1 = input("Student information: ")
file2 = input("Exercises information: ")

student_dict = create_student_dict(file1)
exercises_dict = create_exercises_dict(file2)
#print(student_dict)
#print(exercises_dict)
combined_output(student_dict, exercises_dict)

