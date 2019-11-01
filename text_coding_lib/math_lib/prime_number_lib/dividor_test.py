def dividor_test(up_to): #Uses the dividor test. Requires a maximum number.
    up_to_n = up_to+1
    prime = [2] #Inititalization of the prime number space.
    lenght = len(prime) #Gets object count in prime.
    #print(lenght)
    tested_primes = 0 #Saves the number of already tested primes.
    current = 3 #Current number
    loop = True #Starts the loop

    while loop == True: #This is the real funktion.
        if up_to_n != current:
            if tested_primes < lenght:
                #print(1)
                if current%prime[tested_primes] != 0:
                    #print(1.1)
                    tested_primes = tested_primes+1
                elif current%prime[tested_primes] == 0:
                    #print(current%prime[tested_primes])
                    #print(1.2)
                    tested_primes = 0
                    current = current+1
            elif tested_primes >= lenght:
                #print(2)
                prime.append(current)
                tested_primes = 0
                current = current+1
                lenght = len(prime)
                #print(prime)
        elif up_to_n == current:
            loop = False
            print(prime)
            print("Finished")
