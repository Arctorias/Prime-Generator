def find_number_of_bits(number: int)-> int:
    bits= 0
    while number:
        number >>= 1
        bits +=1
    return bits