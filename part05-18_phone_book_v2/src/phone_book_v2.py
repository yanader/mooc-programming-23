# Write your solution here
def user_input():
    phonebook = {}
    while True:
        command = input('command (1 search, 2 add, 3 quit): ')
        if command == '3':
            print('quitting...')
            break
        if command == '2':
            add(phonebook)
        if command == '1':
            search(phonebook)


def add(book: dict):
    name = input('name: ')
    number = input('number: ')
    if name in book:
        book[name].append(number)
    else:
        ls = [number]
        book[name] = ls
    print('ok!')
    
def search(book: dict):
    name = input('name: ')
    if name not in book:
        print('no number')
        return
    else:
        for number in book[name]:
            print(number)


#if __name__ == "__main__":
user_input()