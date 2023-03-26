# write your solution here
def read_fruits():
    fruitDictionary = {}
    with open('fruits.csv') as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            itemsList = line.split(';')
            fruitDictionary[itemsList[0]] = float(itemsList[1])
    return fruitDictionary

if __name__ == "__main__":
    print(read_fruits())