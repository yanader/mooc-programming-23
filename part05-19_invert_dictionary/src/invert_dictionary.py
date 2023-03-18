def invert(dictionary: dict):
    temp = {}

    for key in dictionary:
        temp[dictionary[key]] = key
    
    dictionary.clear()

    for key in temp:
        dictionary[key] = temp[key]
##we can do the above by either just iterating over the keys
## or by iterating over the 'key, value's in dictionary.items()
# depending on which we choose changes how we refer to each value


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    print(s)
    invert(s)
    print(s)