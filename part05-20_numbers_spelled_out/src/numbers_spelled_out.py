# Write your solution here
def dict_of_numbers() -> dict:
    new_dictionary = {}
    singles = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',18:'eighteen'}
    prefixes = {20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

    i = 0
    while i < 100:
        if i in singles:
            new_dictionary[i] = singles[i]
        elif i in teens:
            new_dictionary[i] = teens[i]
        elif i < 20:
            new_dictionary[i] = (singles[i%10] + 'teen')
        else:
            if i % 10 == 0:
                new_dictionary[i] = prefixes[i]
            else:
                new_dictionary[i] = (prefixes[i//10*10]) + '-' + (singles[i%10])
        i+=1
    return new_dictionary

if __name__ == "__main__":
    numbers = dict_of_numbers()
    #for i in range (10,30,3):
    print(numbers[18])