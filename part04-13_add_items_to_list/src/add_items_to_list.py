# Write your solution here
valueCount = int(input('How many items:'))

ls = []
i = 0
while i < valueCount:
    x = int(input(f'Item {i+1}:'))
    ls.append(x)
    i+=1
print(ls)