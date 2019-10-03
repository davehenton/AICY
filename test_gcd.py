def greatest_common_divisor(smaller_number,greater_number): #Gets the gcd of two numbers.
    loop="true"
    while loop=="true": #Calculates the gcd.
        tmp_divisor = greater_number//smaller_number #Dived the greater trough the smaler number without rest.
        tmp_rest = greater_number%smaller_number #Dived the greater trough the smaller number and takes the rest.
        if (tmp_rest==0): #If gcd was found, break loop
            gcd=smaller_number
            loop="false"
            break
        else: #If gcd wasn't found, do again.
            greater_number = smaller_number
            smaller_number = tmp_rest

    #print(gcd)
    return(gcd) #Return gcd.
