# Write your solution here
def read_input(s:str, x:int, y:int):
    while True:
        try:
            input_number = input(s)
            number = int(input_number)
            if number >= x and number <= y:
                return number
        except:
            pass
        print('You must type in an integer between ' + str(x) + ' and ' + str(y))

# number = read_input("Please type in a number: ",5, 15)
# print('You typed in:', number)