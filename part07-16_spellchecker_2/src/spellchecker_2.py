from difflib import get_close_matches


text = input('write text: ')
words = text.split(' ')
incorrect_words = []
sentence = ''

with open('wordlist.txt') as word_file:
    contents = word_file.read()
    contents_list = contents.split('\n')
    word_file.close()
    
for word in words:
    if word.lower() in contents_list:
        sentence += word + ' '
    else:
        incorrect_words.append(word)
        sentence += '*' + word + '* '
    

print(sentence)
print('suggestions:')
for word in incorrect_words:
    close_match1 = get_close_matches(word, contents_list)[0]
    close_match2 = get_close_matches(word, contents_list)[1]
    close_match3 = get_close_matches(word, contents_list)[2]
    print(word + ': ' + close_match1 + ', ' + close_match2 + ', ' + close_match3)

    