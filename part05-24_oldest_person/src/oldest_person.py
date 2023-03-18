# Write your solution here
def oldest_person(people: list):
    name = ""
    year = 3000
    for person in people:
        if person[1] <  year:
            year = person[1]
            name = person[0]
    return name

#people_list = [("Arthur", 1977), ("Emily", 2014)]
#result = oldest_person(people_list)
#print(result)