import urllib.request
import json
import certifi

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(address, cafile=certifi.where())
    data = request.read()
    course_list = json.loads(data)
    return_list = []

    for course in course_list:
        if course['enabled']:
            exercises = 0
            for ex in course["exercises"]:
                exercises += ex
            return_list.append((course["fullName"],course["name"],course["year"],exercises))
    return return_list

def retrieve_course(course_name:str):
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    request = urllib.request.urlopen(address, cafile=certifi.where())
    data = request.read()
    course_list = json.loads(data)
    
    students_count = 0
    hours_count = 0
    exercise_count = 0
    course_dict = {}
    course_dict['weeks'] = len(course_list)
    for week in course_list:
        if course_list.get(week).get('students') > students_count:
            students_count = course_list.get(week).get('students')
        hours_count += course_list.get(week).get('hour_total')
        exercise_count += course_list.get(week).get('exercise_total')
    course_dict['students'] = students_count
    course_dict['hours'] = hours_count
    course_dict['hours_average'] = hours_count // students_count
    course_dict['exercises'] = exercise_count
    course_dict['exercises_average'] = exercise_count // students_count

    return course_dict

if __name__ == "__main__":
    print(retrieve_course('docker2019'))