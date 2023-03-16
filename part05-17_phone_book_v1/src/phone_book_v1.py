# Write your solution here
def user_input():
    phonebook = {}
    while True:
        command = int(input('command (1 search, 2 add, 3 quit): '))
        if command == 3:
            break
        elif command == 2:
            add(phonebook)
        elif command == 1:
            search(phonebook)
    print('quitting...')

def search(book: dict):
    name_to_search  = input('name: ')
    if name_to_search in book:
        print(book[name_to_search])
    else:
        print('no number')

def add(book: dict):
    name_to_add = input('name: ')
    number = input('number: ')
    book[name_to_add] = number
    print('ok!')

user_input()