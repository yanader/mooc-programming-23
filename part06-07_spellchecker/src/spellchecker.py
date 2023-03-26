# write your solution here
input_line = input('Write text:')

with open('wordlist.txt') as new_file:
    contents = new_file.read()
    contents_list = contents.split('\n')
    input_list = input_line.split(' ')
    output = ''
    for word in input_list:
        if word.lower() in contents_list:
            output += word + ' '
        else:
            output += '*' + word + '* '
    output = output.strip()

print(output)
            