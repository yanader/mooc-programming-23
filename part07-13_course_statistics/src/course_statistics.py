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

if __name__ == "__main__":
    retrieve_course('docker2019')