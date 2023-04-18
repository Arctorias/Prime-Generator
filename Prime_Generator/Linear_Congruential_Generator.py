class Linear_Congruential_Generator_Algorithm :
    def __init__(self,seed: int =1, number_of_bits: int = 32, a:int = 1664525, c : int = 1013904223) -> None:
        self.a = a
        self.c = c
        self.m = 2 ** number_of_bits
        self.state = seed
        self.number_of_bits = number_of_bits

    def __m__(self, number_of_bits: int):                       # Sets variable M as a power of 2, in this case "2**number_of_bits"
        self.m = 2 ** number_of_bits
        self.number_of_bits = number_of_bits
        

    def generate(self, is_prime: bool = False):
        
        self.state = (self.a * self.state + self.c) % self.m    # Python code for the algorithm formula : X_n+1 = (a*X_n-c)mod m

        while self.state < (2**(self.number_of_bits - 1)):      # Keeps iterating till the most significant bit is 1
            self.state = (self.a * self.state + self.c) % self.m
        
        if is_prime:                                            # Guarantees no pair numbers if asking for primes
            return self.state | 1
        
        return self.state