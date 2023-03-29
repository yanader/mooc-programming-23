import re
# Write your solution here
def find_words(search_term: str):
    results_list = []
    with open('words.txt') as new_file:
        if search_term[0] == '*':
            for line in new_file:
                if line[:-1].endswith(search_term[1:]):
                    results_list.append(line[:-1])
        elif search_term[-1] == '*':
            for line in new_file:
                if line[:-1].startswith(search_term[:-1]):
                    results_list.append(line[:-1])
        elif '.' in search_term:
            for line in new_file:
                if compare_dot(search_term, line[:-1]):
                    results_list.append(line[:-1])
        else:
            for line in new_file:
                if line[:-1] == search_term:
                    results_list.append(search_term)
        new_file.close()
    return results_list


def compare_dot(search_term: str, word: str):
    match = True
    if len(search_term) != len(word):
        return False
    for i in range(len(word)):
        if search_term[i] != word[i] and search_term[i] != '.':
            match = False
    return match

if __name__ == "__main__":
    print(find_words(".a.e"))


