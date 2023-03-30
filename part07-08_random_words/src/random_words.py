import random

def words(n: int, beginning: str):
    word_list = []
    with open('words.txt') as new_file:
        for line in new_file:
            if line.startswith(beginning):
                word_list.append(line.strip())
    if len(word_list) < n:
        raise ValueError
    else:
        random.shuffle(word_list)
        return_list = []
        for i in range(n):
            return_list.append(word_list[i])
    
    return return_list


if __name__ == "__main__":
    print(words(10,'sta'))