# Write your solution here
ls = []

while True:
    word = input('Word:')
    if ls.count(word) > 0:
        break
    else:
        ls.append(word)
print(f'You typed in {len(ls)} different words')