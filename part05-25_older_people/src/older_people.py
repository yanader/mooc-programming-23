def older_people(people: list, year: int):
    return_list = []
    for person in people:
        if person[1] < year:
            return_list.append(person[0])
    return return_list

