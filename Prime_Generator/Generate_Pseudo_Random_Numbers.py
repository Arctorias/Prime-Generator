from BlumBlumShub import BlumBlumShub_Algorithm
from Linear_Congruential_Generator import Linear_Congruential_Generator_Algorithm
from utils import find_number_of_bits
import time

amount_of_numbers_to_be_generated = 1000
number_of_bits_by_number = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

seed =  int(time.time())
bbs = BlumBlumShub_Algorithm(seed=seed)
lcg = Linear_Congruential_Generator_Algorithm(seed=seed)


with open("./Pseudo_random_numbers.txt", "w") as writer:

    writer.write("BLUMBLUMSHUB PSEUDO-RANDOM NUMBERS:\n")
    for number_of_bits in number_of_bits_by_number:

        average_time = 0.0

        writer.write(f"Generating {number_of_bits} bits\n")
        for _ in range(amount_of_numbers_to_be_generated):

            start = time.time()
            generated_number = bbs.generate_numbers(number_of_bits=number_of_bits)
            final = time.time()


            bits = find_number_of_bits(generated_number) #These two lines check if there were enough bits in the "generated_number" variable
            assert(number_of_bits == bits)

            time_to_generate = final - start
            average_time += (time_to_generate / amount_of_numbers_to_be_generated)

            writer.write(f"{bits} bits took {time_to_generate} seconds\n")
        writer.write(f"The average time to generate {number_of_bits} bits number was {average_time} seconds\n")

    writer.write("LINEAR CONGRUENTIAL GENERATOR PSEUDO-RANDOM NUMBERS:\n")
    
    for number_of_bits in number_of_bits_by_number:

        average_time = 0.0
        lcg.__m__(number_of_bits)

        writer.write(f"Generating {number_of_bits} bits\n")
        for _ in range(amount_of_numbers_to_be_generated):

            start = time.time()
            generated_number = lcg.generate()
            final = time.time()

            bits = find_number_of_bits(generated_number) #These two lines check if there were enough bits in the "generated_number" variable
            assert(number_of_bits == bits)

            time_to_generate = final - start
            average_time += (time_to_generate / amount_of_numbers_to_be_generated)

            writer.write(f"{bits} bits took {time_to_generate} seconds\n")
        writer.write(f"The average time to generate {number_of_bits} bits number was {average_time} seconds\n")