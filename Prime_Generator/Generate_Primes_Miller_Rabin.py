from BlumBlumShub import BlumBlumShub_Algorithm
from Linear_Congruential_Generator import Linear_Congruential_Generator_Algorithm
from Miller_Rabin import Miller_Rabin_Algorithm
from typing import Dict, List
from utils import find_number_of_bits
import time

number_of_bits_by_number = [40, 56, 80, 128, 168, 224]
quantity_of_numbers = 10

seed =  int(time.time())
bbs = BlumBlumShub_Algorithm(seed=seed)
lcg = Linear_Congruential_Generator_Algorithm(seed=seed)

possible_primes : Dict[int, List[int]] = {}

for number_of_bits in number_of_bits_by_number: # Possible primes List
    possible_primes[number_of_bits] = []

with open("./Miller_Rabin_Prime_numbers.txt", "w") as writer:

    writer.write("BLUMBLUMSHUB PRIME NUMBERS:\n")
    for number_of_bits in number_of_bits_by_number:

        average_time = 0.0

        writer.write(f"Generating prime numbers with {number_of_bits} bits\n")
        for _ in range(quantity_of_numbers):

            start = time.time()

            generated_number = bbs.generate_numbers(number_of_bits=number_of_bits)

            while not Miller_Rabin_Algorithm(generated_number):    # Checks if its prime, if not, keeps generating numbers
                generated_number = bbs.generate_numbers(number_of_bits=number_of_bits, is_prime=True)
            
            final = time.time()

            bits = find_number_of_bits( generated_number)   #These two lines check if there were enough bits in the "generated_number" variable
            assert(number_of_bits == bits)

            time_to_generate = final - start
            average_time += (time_to_generate/quantity_of_numbers)

            possible_primes[number_of_bits].append(generated_number)  # adds possible prime to list

            writer.write(f"{bits} bits took {time_to_generate} seconds\n")
        writer.write(f"The average time to generate {number_of_bits} bits prime number was {average_time} seconds\n")

    writer.write(possible_primes.__str__())

    writer.write("LINEAR CONGRUENTIAL GENERATOR PRIME NUMBERS:\n")
    for number_of_bits in number_of_bits_by_number:

        lcg.__m__(number_of_bits)

        average_time = 0.0

        writer.write(f"Generating prime numbers with {number_of_bits} bits\n")
        for _ in range(quantity_of_numbers):

            start = time.time()

            generated_number=lcg.generate()

            while not Miller_Rabin_Algorithm(generated_number):   # Checks if its prime, if not, keeps generating numbers
                generated_number = lcg.generate(is_prime=True)
            
            final = time.time()

            bits = find_number_of_bits(generated_number)   #These two lines check if there were enough bits in the "generated_number" variable
            assert(number_of_bits == bits)

            time_to_generate = final - start
            average_time += (time_to_generate/quantity_of_numbers)

            possible_primes[number_of_bits].append(generated_number)  # adds possible prime to list

            writer.write(f"{bits} bits took {time_to_generate} seconds\n")
        writer.write(f"The average time to generate {number_of_bits} bits prime number was {average_time} seconds\n")