# Write your solution here
def prime_numbers():
    i = 2
    while True:
        if i == 2:
            yield i
            i+=1
            
        is_prime = True
        for x in range(2,i):
            if i % x == 0:
                is_prime = False
        
        if is_prime:
            yield i
        i +=1
        