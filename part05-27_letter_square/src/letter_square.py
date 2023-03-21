
size = int(input('Layers:'))
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
square_side_len = size * 2 - 1
square_mid = (square_side_len // 2) 

i = 0
while i < square_mid+1:
    print(letters[size-1:size-1-i:-1] + ((square_side_len - (2*i)) * letters[size-1-i]) + letters[size-i:size:1])
    i+=1
j = 0
while j < size-1:
    print( letters[size-1:1+j:-1] + ((3+(2*j)) * letters[1+j]) + letters[j+2:size:1] ) 
    j+=1

