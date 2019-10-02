def main():

    # Get maximum numbers of prims.

    while True:
        try:
            maximum = int(input('Maximum: '))
            #maximum = int(10)
            print(maximum)
            break

        except ValueError:
            print("Not allowed! Use an Integer as Input!")

    numbers = [True]*(maximum+1)
    #Remove 0 and 1
    numbers[0] = False
    numbers[1] = False
    a = []

    i = 2
    while i*i <= maximum:
        if numbers[i] == True:
            #Mark number as prim
            #Kill all multiplie of prim.
            for k in range(i*i,maximum+1,i):
                numbers[k] = False

        i = i+1

        # Ausgabe aller gefundenen Zahlen
    for i, v in enumerate(numbers):
        if v == True:
            a.append(i)
            print (i, ',')

    #print(a)
    with open('C:/Users/nicip/github/AICY/Output.py', 'w') as f:
        f.write("zahl=[")
        for item in a:
            f.write("%s," % item)
        f.write("1]")
        f.close()
        print('done')
    return 0

if __name__ == '__main__':
    main()
