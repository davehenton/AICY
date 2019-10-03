from v_big_numbers import prim_gen_min as pgmi, prim_gen_max as pgma
from test_random_number_odd import gen_n
from random_int_gen import GenRandom
from find_gcd import greatest_common_divisor

def Prime_gen():
    loop = "true"
    while loop=='true': #Loop breakes, if a prime number is found.
        random_number_n = gen_n(pgmi,pgma) #Generates an odd, random, 150 digits, positive number.
        loop2 = 10
        while loop2>=1:
            random_number_a = GenRandom(2,random_number_n-1) #Generates a random positive number, that is smaller than random_number_n.
            gcd = greatest_common_divisor(random_number_a, random_number_n)
            print(random_number_n)
            if gcd == 1:
                prim_number = random_number_n
                loop2 = loop2-1
            else:
                print('Error: ' + str(gcd))
                loop2 = 0
        loop = "false"

    return(prim_number)
