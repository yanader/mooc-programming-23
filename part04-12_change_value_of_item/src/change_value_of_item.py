# Write your solution here
ls = [1,2,3,4,5]

while True:
    index = int(input('Index:'))
    if index == -1:
        break
    value = int(input('New value:'))
    ls[index] = value
    print(ls)
