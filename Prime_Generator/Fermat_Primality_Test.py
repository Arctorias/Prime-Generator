from random import randint


def Fermat_Primality_Test_Algorithm(n: int, k: int =100) -> bool:

    if n in [2,3]:  # Base case
        return True

    if n < 2:       # Guarantees no number smaller than 2
        return False
    
    if n%2 == 0:    # Guarantees no pair numbers
        return False
    
    for _ in range(k):
        
        a = randint(2, n - 2)   # Gets a random value between 2 and n-2

        if pow(a, n - 1,n) != 1:   # If a^(n-1) != 1(Mod n), then the number is composite
            return False
    
    return True