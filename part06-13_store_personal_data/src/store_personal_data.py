# Write your solution here

def store_personal_data(person: tuple):
    with open('people.csv','a') as filename:
        filename.write(str(person[0]) + ';' + str(person[1]) + ';' + str(person[2]) + '\n')
        filename.close()