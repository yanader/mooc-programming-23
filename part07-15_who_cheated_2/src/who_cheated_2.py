from datetime import datetime, timedelta

def create_student_data():
    students = {}
    with open('start_times.csv') as start_file:
        for line in start_file:
            parts = line.replace('\n','').split(';')
            students[parts[0]] = [parts[1],{}]
        start_file.close()

    with open('submissions.csv') as submission_file:
        for line in submission_file:
            parts = line.replace('\n','').split(';')
            if new_score_larger(students, parts[0],parts[1],parts[2]) and not took_more_than_three_hours(students.get(parts[0])[0], parts[3]):
                students.get(parts[0])[1][parts[1]] = parts[2]
        submission_file.close()
    
    return students

def final_points():
    detailed_dictionary = create_student_data()
    total_points = {}
    for student, scores in detailed_dictionary.items():
        total_points[student] = add_up_points(scores[1])
    return total_points

def add_up_points(scores: dict):
    total = 0
    for task, score in scores.items():
        total += int(score)
    return total

def new_score_larger(stud_dict: dict, name:str, task: int, score: int):
    try:
        return score > stud_dict.get(name)[1].get(task)
    except:
        return True
    
def took_more_than_three_hours(start_time:str, submit_time:str) -> int:
    start_parts = start_time.split(':')
    submit_parts = submit_time.split(':')
    start = datetime(2000,1,1,int(start_parts[0]),int(start_parts[1]))
    submit = datetime(2000,1,1,int(submit_parts[0]),int(submit_parts[1]))
    return start + timedelta(minutes=180) < submit

if __name__ == "__main__":
    
    ##print(create_student_data())
    #print(final_points())
    final_points()