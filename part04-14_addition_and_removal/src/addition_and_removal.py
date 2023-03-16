# Write your solution here
ls = []
i = 1
while True:
    print(f'The list is now {ls}')
    command = input('a(d)d, (r)emove or e(x)it:')
    if command == 'x':
        break
    if command == 'd':
        ls.append(i)
        i+=1
    elif command == 'r':
        i = ls.pop(len(ls)-1)
print('Bye!')