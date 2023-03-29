def read_file(filename):
    with open(filename) as file:
        print('Entries:')
        for line in file:
            print(line.replace('\n',''))
        file.close()

def update_file(filename, entry):
    with open(filename,'a') as file:
        file.write(entry + '\n')
        file.close()

filename = 'diary.txt'
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    command = int(input('Function: '))
    if command == 0:
        print('Bye now!')
        break
    if command == 1:
        entry = input('Diary entry: ')
        update_file(filename, entry)
    if command == 2:
        read_file(filename)