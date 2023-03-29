from string import ascii_letters, punctuation


def separate_characters(my_string:str):
    ascii_string = ''
    punctuation_string = ''
    other_string = ''
    for c in my_string:
        if c in ascii_letters:
            ascii_string += c
        elif c in punctuation:
            punctuation_string += c
        else:
            other_string += c
    return (ascii_string, punctuation_string, other_string)




