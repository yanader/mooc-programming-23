# Write your solution here
def remove_smallest(numbers: list):
    indexOfSmallest = 0
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            indexOfSmallest = i
            smallest = numbers[i]
    numbers.remove(smallest)
    #alt could use 
    # del numbers[indexOfSmallest]
