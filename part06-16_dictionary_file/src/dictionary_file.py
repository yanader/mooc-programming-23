
def add_word(finnish_word:str, english_word:str):
    with open('dictionary.txt','a') as new_file:
        new_file.write(finnish_word + ';' + english_word + '\n')
        new_file.close()
    print('Dictionary entry added')

def search_word(search_term: str):
    with open('dictionary.txt') as new_file:
        for line in new_file:
            parts = line.strip().split(';')
            if search_term in parts[0] or search_term in parts[1]:
                print(parts[0] + ' - ' + parts[1])

while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    command = int(input('Function: '))
    if command == 3:
        print('Bye!')
        break
    if command == 1:
        finnish_word = input('The word in Finnish: ')
        english_word = input('The word in English: ')
        add_word(finnish_word, english_word)
    if command == 2:
        search_term = input('Search term: ')
        search_word(search_term)