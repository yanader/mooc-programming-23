from datetime import datetime, timedelta

def create_student_data():
    students = {}
    with open('start_times.csv') as start_file:
        for line in start_file:
            parts = line.replace('\n','').split(';')
            students[parts[0]] = [parts[1],[]]
        start_file.close()

    with open('submissions.csv') as submission_file:
        for line in submission_file:
            parts = line.replace('\n','').split(';')
            students[parts[0]][1].append(parts[3])
        submission_file.close()
    
    return students

def took_more_than_three_hours(start_time:str, submit_time:str) -> int:
    start_parts = start_time.split(':')
    submit_parts = submit_time.split(':')
    start = datetime(2000,1,1,int(start_parts[0]),int(start_parts[1]))
    submit = datetime(2000,1,1,int(submit_parts[0]),int(submit_parts[1]))
    return start + timedelta(minutes=180) < submit

def cheaters():
    student_data = create_student_data()
    cheater_list = []
    for student, times in student_data.items():
        #print(student + ' - '+ str(times[0]) +' - ' + str(min(times[1])))
        if took_more_than_three_hours(times[0], max(times[1])):
            cheater_list.append(student)
            continue
    return cheater_list


if __name__ == "__main__":
    print(cheaters())
    # data = create_student_data()
    # for student, times in data.items():
    #     print(student)
    #     print(times[1])

