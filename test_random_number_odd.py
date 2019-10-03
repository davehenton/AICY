from random_int_gen import GenRandom
from v_big_numbers import prim_gen_min as pgmi, prim_gen_max as pgma


def gen_n(): #Generates n new until it is odd. Doesn't require any input.
    loop = "true"
    while loop=="true":
        random_number_n = GenRandom(pgmi,pgma) #Gives Funktion GenRandom pgmi and pgma as input.
        #print(random_number_n)
        tmp_modulo_result = random_number_n%2 #Divides Output of GenRandom with 2.
        if tmp_modulo_result==1: #Breaks the Loop if random_number_n is odd.
            loop="false"

    return random_number_n #Returns random_number_n.
