from math import gcd

class BlumBlumShub_Algorithm:
    def __init__(self,seed: int= 1, p: int =3141592653589771, q: int = 2718281828459051) -> None:
        # A bunch of checks to see if P and Q fit the restrictions 
        if p == q:
            raise ValueError("P and Q cannot be equal")

        if gcd(p,q) != 1:
            raise ValueError("P and Q  must be co-primes AKA gcd(P,Q) = 1")

        if p%4 != 3 or q % 4 != 3:
            raise ValueError("P and Q must be congruential to 3 (mod 4)")

        self.m = p*q  # M = p* q
        self.state = seed
    
    def next_bit(self): # Generate next bit

        self.state = pow(self.state, 2, self.m) # Python code for the algorithms formula : X_n+1 = (X_n^2)mod m
        
        return self.state % 2   
    
    def generate_numbers(self, number_of_bits: int, is_prime: bool = False)->int: # Generate number with "number_of_bits" bits
        number = 0
        for _ in range(number_of_bits):
            number = (number<<1) | self.next_bit()

        if number < (2**(number_of_bits - 1)):        # If the number doesnt have the necessary number of bits, it puts 1 on the most significant bit
            return self.generate_numbers(number_of_bits, is_prime)
        
        if is_prime:                                  # Guarantees no pair numbers if asking for primes
            return number | 1

        return number