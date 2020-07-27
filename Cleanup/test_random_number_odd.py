#from random_int_gen import GenRandom

def gen_n(minimal_number,maximal_number): #Generates n new until it is odd. Doesn't require any input.
    loop = "true"
    while loop=="true":
        #random_number_n = GenRandom(minimal_number,maximal_number) #Gives Funktion GenRandom minimal and maximal number as input.
        random_number_n = 20
        #print(random_number_n)
        tmp_modulo_result = random_number_n%2 #Divides Output of GenRandom with 2.
        if tmp_modulo_result==1: #Breaks the Loop if random_number_n is odd.
            loop="false"

    return random_number_n #Returns random_number_n.
