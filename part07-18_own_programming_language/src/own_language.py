# Write your solution here

def run(program):
    variables = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,}
    return_list = []
    step = 0
    location_dict = {}
    for index, item in enumerate(program):
        if item[-1] == ':':
            set_location(location_dict, item[:-1], index)

    while step < len(program):
        parts = program[step].split(' ')
        command = parts[0]

        if command == 'PRINT':
            print_command(return_list, variables, parts[1])
        elif command == 'MOV':
            mov_command(variables, parts[1], parts[2])
        elif command == 'ADD':
            #print('executing add')
            add_command(variables, parts[1], parts[2])
        elif command == 'SUB':
            sub_command(variables, parts[1], parts[2])
        elif command == 'MUL':
            mul_command(variables, parts[1], parts[2])
        elif command == 'JUMP':
            step = jump_command(location_dict, parts[1])
        elif command == 'IF':
            new_step = conditional_command(variables, parts[1], parts[2], parts[3], location_dict, parts[5])
            if new_step != -1:
                step = new_step

        step+=1
    return return_list


def print_command(return_list:list, variables:dict, input:str):
    if input in variables.keys():
        return_list.append(variables.get(input))
    else:
        return_list.append(int(input))

def mov_command(variables:dict, variable_to_change: str, change_value:str):
    if change_value in variables.keys():
        val = variables.get(change_value)
    else:
        val = int(change_value)
    variables[variable_to_change] = int(val)
    
def add_command(variables:dict, variable_to_change: str, add_value: str):
    if add_value in variables.keys():
        val = variables.get(add_value)
    else:
        val = int(add_value)
    variables[variable_to_change] += val

def sub_command(variables:dict, variable_to_change: str, sub_value: str):
    if sub_value in variables.keys():
        val = variables.get(sub_value)
    else:
        val = int(sub_value)
    variables[variable_to_change] -= val
    
def mul_command(variables:dict, variable_to_change: str, mul_value: str):
    if mul_value in variables.keys():
        val = variables.get(mul_value)
    else:
        val = int(mul_value)
    variables[variable_to_change] *= val

def set_location(location_dict:dict, location_name:str, loction:int):
    location_dict[location_name] = loction

def jump_command(location_dict:dict, location_name:str) -> int:
    return location_dict.get(location_name)

def conditional_command(variables: dict, value1:str, operator:str, value2: str, location_dict:dict, destination: str):
    operator_string = operator
    if value1 in variables.keys():
        item1 = variables.get(value1)
    else:
        item1 = value1
    if value2 in variables.keys():
        item2 = variables.get(value2)
    else:
        item2 = value2

    result = eval(f"{item1} {operator_string} {item2}")
    if result:
        return jump_command(location_dict, destination)
    else:
        return -1

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)