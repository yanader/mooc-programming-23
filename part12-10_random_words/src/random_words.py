from random import choice
def word_generator(characters:str, length:int, amount:int):
    i = 0
    while i < amount:
        yield "".join([choice(characters) for i in range(length)])
        i+=1



# wordgen = word_generator("abcdefg", 3, 5)
# for word in wordgen:
#     print(word)