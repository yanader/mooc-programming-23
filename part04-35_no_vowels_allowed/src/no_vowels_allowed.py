# Write your solution here
def no_vowels(str: str):
    #new_string = str.replace('a','')
    #new_string = new_string.replace('e','')
    #new_string = new_string.replace('i','')
    #new_string = new_string.replace('o','')
    #new_string = new_string.replace('u','')
    vowels = 'aeiou'
    new_string = ''

    for letter in str:
        if letter not in vowels:
            new_string+=letter
    
    return new_string

if __name__ == "__main__":
    print(no_vowels("Stephen Barrow"))