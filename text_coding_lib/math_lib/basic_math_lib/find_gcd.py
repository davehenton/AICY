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
