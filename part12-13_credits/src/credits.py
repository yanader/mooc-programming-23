from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


def sum_of_all_credits(attempts:list):
    #return reduce(credit_sum_helper, attempts, 0)
    return reduce(lambda credit_sum, attempt : credit_sum + attempt.credits, attempts, 0)

def credit_sum_helper(credit_sum, attempt):
    return credit_sum + attempt.credits

def sum_of_passed_credits(attempts:list):
    return reduce(lambda credit_sum, attempt:credit_sum + attempt.credits, filter(lambda CourseAttempt:CourseAttempt.grade > 0, attempts) ,0)
    #return filter(lambda CourseAttempt:CourseAttempt.grade > 0, attempts)
    #return reduce(passed_credits_helper, attempts, 0)
    

def passed_credits_helper(passed_credits_sum, attempt):
    if attempt.grade >= 1:
        return passed_credits_sum + attempt.credits
    else:
        return passed_credits_sum

def average(attempts:list):
    return reduce(lambda grade_sum, attempt: grade_sum + attempt.grade, filter(lambda CourseAttempt:CourseAttempt.grade>0, attempts), 0)/len(list(filter(lambda CourseAttempt:CourseAttempt.grade>0, attempts)))
    
