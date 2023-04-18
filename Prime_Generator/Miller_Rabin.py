from random import randint

def decompose_number(n: int):
    r = 0

    while n%2 == 0: # Checks if number has any power of 2
        n = n / 2   
        r += 1      # Increments the power
    
    return r, n

def Miller_Rabin_Algorithm(n: int, k: int =100)-> bool:

    if n in [2,3]:  # Base case
        return True
    
    if n < 2:       # Guarantees no number smaller than 2
        return False
    
    if n%2 == 0:    # Guarantees no pair numbers
        return False
    
    r,d = decompose_number(n-1)   # Decomposes N as 2^r*d+1, with d being odd

    for _ in range(k):
        
        a = randint(2,n-2)   # Gets a random value between 2 and n-2, with n being a probable prime
        x = pow(a,d,n)        # Python code for the algorithms formula : a^d*mod n

        if x in (1, n - 1):
            continue
        
        continue_loop = False
        for _ in range(r - 1):

            x = pow(x, 2, n)    # Python code for the algorithms formula : x= x^2 mod n

            if x == n - 1:
                continue_loop = True
        
        if continue_loop: continue

        return False            # Returns false, because its a composite number

    return True