import json

def print_persons(filename:str):
    with open(filename) as new_file:
        stud_dict = json.load(new_file)

    for student in stud_dict:
        hobbies = ''
        for hobby in student["hobbies"]:
            hobbies += hobby + ', '
        print(student["name"]+ ' '  + str(student["age"]) + ' years ' + '(' + hobbies[:-2] + ')')

if __name__ == "__main__":
    print_persons('file1.json')