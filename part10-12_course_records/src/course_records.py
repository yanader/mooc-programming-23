# tee ratkaisusi tänne

class Course:
    def __init__(self, name:str, grade:int, credits:int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits
    
    def name(self):
        return self.__name

    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__credits
    
    def change_grade(self, new_grade:int):
        if new_grade > self.grade():
            self.__grade = new_grade
    
    def __str__(self):
        return f'{self.__name} ({self.__credits} cr) grade {self.__grade}'

class CourseBook:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, name:str, grade:int, credits:int):
        if not name in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].change_grade(grade)
    
    def change_grade(self, name:str, new_grade:int):
        self.__courses[name].change_grade(new_grade)
    
    def get_course(self, name:str):
        if not name in self.__courses:
            return None
        else:
            return self.__courses[name]
    
    def stats(self):
        complete = len(self.__courses)
        total_grades = 0
        total_credits = 0
        distribution = {1:0, 2:0, 3:0, 4:0, 5:0}
        for course in self.__courses:
            total_grades += self.__courses[course].grade()
            total_credits += self.__courses[course].credits()
            distribution[self.__courses[course].grade()] += 1
        print(f'{complete} completed courses, a total of {total_credits} credits')
        print(f'mean {total_grades / complete:.1f}')
        print('grade distribution')
        for i in range(5,0,-1):
            print(str(i) + ': ' + 'x'*distribution[i])

class CourseApplication:
    def __init__(self):
        self.__coursebook = CourseBook()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__coursebook.add_course(course, grade, credits)

    def get_course(self):
        course = input("course: ")
        if self.__coursebook.get_course(course) == None:
            print("no entry for this course")
        else:
            print(self.__coursebook.get_course(course))
            
    def get_stats(self):
        self.__coursebook.stats()

    def execute(self):
        self.help()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            if command == 1:
                self.add_course()
            if command == 2:
                self.get_course()
            if command == 3:
                self.get_stats()


#if __name__ == "__main__":
application = CourseApplication()
application.execute()