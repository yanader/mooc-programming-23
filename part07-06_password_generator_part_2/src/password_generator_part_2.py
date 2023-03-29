from string import ascii_lowercase, digits
from random import randint, shuffle

def generate_strong_password(length: int, include_number: bool, special_character:bool):
    password_chars = []
    password_chars.append(ascii_lowercase[randint(1,26)-1])
    punctuation = '!?=+-()#'
    character_list = ascii_lowercase
    if include_number:
        c = digits[randint(1,10)-1]
        password_chars.append(c)
        character_list += digits
    if special_character:
        c = punctuation[randint(1,len(punctuation))-1]
        password_chars.append(c)
        character_list += punctuation
    
    for i in range(length - len(password_chars)):
        c = character_list[randint(1,len(character_list))-1]
        password_chars.append(c)
    shuffle(password_chars)
    return_password = ''
    for c in password_chars:
        return_password += c
    return return_password

if __name__ == "__main__":
    for i in range(10):
        passw = generate_strong_password(2,False, False)
        print(passw)

