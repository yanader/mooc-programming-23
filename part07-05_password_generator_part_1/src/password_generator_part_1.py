from string import ascii_lowercase
from random import randint


def generate_password(length: int):
    password = ''
    for i in range(length):
        letter = ascii_lowercase[randint(1,26)-1]
        password += letter
    return password


##print(generate_password(15))