# Write your solution here
def smallest_average(person1:dict, person2:dict, person3:dict):
    person_list = [person1, person2, person3]
    min_average = 10.0
    return_person = person1

    for person in person_list:
        sum = person.get('result1') + person.get('result2') + person.get('result3')
        average = sum / 3.0
        if average < min_average:
            min_average = average
            return_person = person
            
    return return_person



