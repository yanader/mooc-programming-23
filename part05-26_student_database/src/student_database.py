# Write your solution here
def add_student(database: dict, name: str):
    database[name] = []


def add_course(database: dict, name: str, course: tuple):
    if course[1] == 0:
        return
    course_to_add = course[0]
    score_to_beat = 0
    for completed_course in database[name]:
        if completed_course[0] == course_to_add:
            score_to_beat = completed_course[1]
            break
    if not course_exists(database, name, course):
        database[name].append(course)
    elif course[1] > score_to_beat:
        index_to_remove = index_of_course(database, name, course)
        del database[name][index_to_remove]
        database[name].append((course))



def index_of_course(database: dict, name: str, course: tuple):
    i = 0
    while i < len(database[name]):
        if database[name][i][0] == course[0]:
            return i
        i+=1
    return -1

def summary(database: dict):
    print(f'students {len(database)}')
    name, course_count = most_courses(database)
    print(f'most courses completed {course_count} {name}')
    name, av = best_average(database)
    print(f'best average grade {av} {name}')


def most_courses(database: dict):
    course_count = 0
    name = ''
    for student in database:
        if len(database[student]) > course_count:
            course_count = len(database[student])
            name = student
    return name, course_count

def best_average(database: dict):
    best_av = 0
    name = ''
    for student in database:
        sum = 0
        for course in database[student]:
            sum+= course[1]
        av = sum / len(database[student])
        if av > best_av:
            best_av = av
            name = student
    return name, best_av



def course_exists(database: dict, name: str, course: tuple):
    for completed_course in database[name]:
        if completed_course[0] == course[0]:
            return True
    return False


def print_student(database: dict, name: str):
    if name not in database:
        print(name + ': no such person in the database')
    elif len(database[name]) == 0:
        print(name +':')
        print(' no completed courses')
    else:
        print(name + ':')
        print(' ' + str(len(database[name])) + ' completed courses:')
        points = 0
        for course in database[name]:
            print('  '+course[0]+' '+str(course[1]))
            points += course[1]
        print(' average grade ' + str(points/len(database[name])))



if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")