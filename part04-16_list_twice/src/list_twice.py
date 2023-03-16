ls = []
while True:
    x = int(input('New item:'))
    if x == 0:
        break
    ls.append(x)
    print(f'The list now: {ls}')
    print(f'The list in order: {sorted(ls)}')
print('Bye!')
