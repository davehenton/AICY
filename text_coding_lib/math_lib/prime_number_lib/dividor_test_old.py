def dividor_test():#up_to=10): #Uses the dividor test. Requires a maximum number.
    up_to=10
    prime = [2] #Inititalization of the prime number space.
    lenght = len(prime) #Gets object count in prime.
    print(lenght)
    tested_primes = 0 #Saves the number of already tested primes.
    current = 3 #Current number
    loop = True #Starts the loop
    loop2 = True

    while loop == True: #This is the real funktion.
        if tested_primes >= lenght:
            if current%prime[tested_primes] == current:
                tested_primes = tested_primes+1
            elif current%prime[tested_primes] != current:
                tested_primes = 0
                current = current+1
        elif tested_primes <= lenght:
            prime = prime.append(current)
            loop = False

if __name__ == '__main__':
    dividor_test()
