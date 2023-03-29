# Write your solution here
name = input('Whom should i sign this to: ')
filename = input('Where shall I save it: ')

with open(filename,'w') as new_file:
    new_file.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')