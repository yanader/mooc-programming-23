# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename) as word_file:
        for line in word_file:
            line = line.replace('\n','')
            line_words = line.split(' ')
            for word in line_words:
                word = remove_punctuation(word)
                words.append(word)
    return {word:words.count(word) for word in words if words.count(word) >= lower_limit}


def remove_punctuation(word:str):
    return ''.join([char for char in word if char not in '.,?;:'])
    

#file = 'C:/Users/Ste-PC/AppData/Local/tmc/vscode/mooc-programming-23/part11-12_most_common_words/comprehensions.txt'

#list = most_common_words(file,4)
#print(list)