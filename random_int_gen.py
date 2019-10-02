import random

def GenRandom():    #Generate random number.
    loop = "true"

    while loop=="true":
        n = random.randint(10**149, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        tmp_a = n%2
        if tmp_a==1:
            loop = "false"

    n_m = n

    return n,n_m #n -> Q+ ; n_m=n, but modifiable
