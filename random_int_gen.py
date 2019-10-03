import random

def GenRandom(min_number,max_number):    #Generate random number. Requires smallest and biggest number.
    random_number = random.randint(min_number , max_number)
    return random_number #Returns the random generated number.
