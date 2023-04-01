from string import ascii_letters, digits

def change_case(orig_string:str) -> str:
    return_string = ''
    for c in orig_string:
        if c.isupper():
            return_string += c.lower()
        elif c.islower():
            return_string += c.upper()
        else: 
            return_string += c
    return return_string


def split_in_half(orig_string: str) -> tuple:
    length = len(orig_string) // 2
    return (orig_string[:length],orig_string[length:])


def remove_special_characters(orig_string: str):
    return_string =''
    for c in orig_string:
        if c in digits or c in ascii_letters or c == ' ':
            return_string += c
    return return_string
    


if __name__ == "__main__":
    print(remove_special_characters('abcdefgh.i'))