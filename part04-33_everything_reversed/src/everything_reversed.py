# Write your solution here
def everything_reversed(my_list: list):
    return_list = []
    for str in my_list:
        return_list.append(str[::-1])
    return return_list[::-1]

if __name__ == "__main__":
    print(everything_reversed(['ste','Joy']))