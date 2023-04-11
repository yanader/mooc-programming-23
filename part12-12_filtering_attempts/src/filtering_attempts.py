class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"


def accepted(attempts:list):
    return list(filter(lambda CourseAttempt:CourseAttempt.grade > 0, attempts))

def attempts_with_grade(attempts:list, grade:int):
    return filter(lambda CourseAttempt:CourseAttempt.grade==grade, attempts)

def passed_students(attempts:list, course:str):

    return sorted(list(map(lambda CourseAttempt:CourseAttempt.student_name, 
                           filter(lambda CourseAttempt: CourseAttempt.grade > 0 and CourseAttempt.course_name == course, attempts))))
