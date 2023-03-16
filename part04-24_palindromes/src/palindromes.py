# Write your solution here
def palindromes(str) -> bool:
    left = 0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return False
        left +=1
        right -=1
    return True
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
while True:
    word = input('Please type in a palindrome:')
    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    print("that wasn't a palindrome")
