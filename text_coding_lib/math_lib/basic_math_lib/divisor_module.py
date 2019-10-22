def isOdd(number_to_be_tested): #Returns True if a number is odd and False if not. Will fail if input isn't an INTEGER.
    if number_to_be_tested%2==1:
        return True
    elif number_to_be_tested%2==0:
        return False

def isDivisor(dividend,divisor): #Returns True if the dividend is divisible by the divisor, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%divisor==0:
        return True
    else:
        return False

def threeIsDivisor(dividend): #Returns True if the dividend is divisible by 3, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%3==0:
        return True
    else:
        return False

def fiveIsDivisor(dividend): #Returns True if the dividend is divisible by 5, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%5==0:
        return True
    else:
        return False

def sevenIsDivisor(dividend): #Returns True if the dividend is divisible by 7, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%7==0:
        return True
    else:
        return False

def elevenIsDivisor(dividend):#Returns True if the dividend is divisible by 11, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%11==0:
        return True
    else:
        return False

def thirteenIsDivisor(dividend): #Returns True if the dividend is divisible by 13, else it returns False. Will fail as soon as one of the inputs isn't an INTEGER.
    if dividend%13==0:
        return True
    else:
        return False

def greatest_common_divisor(number_one,number_two): #Gets the gcd of two numbers.
    loop="true"
    while loop=="true": #Calculates the gcd.
        tmp_divisor = number_two//number_one #Dived the greater trough the smaler number without rest.
        tmp_rest = number_two%number_one #Dived the greater trough the smaller number and takes the rest.
        if (tmp_rest==0): #If gcd was found, break the loop.
            gcd=number_one
            loop="false"
            break
        else: #If gcd wasn't found, do the steps above again.
            number_two = number_one
            number_one = tmp_rest

    return(gcd) #Return gcd.
