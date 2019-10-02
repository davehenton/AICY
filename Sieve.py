def main():

    # Get maximum numbers of prims.

    while true:
        try:
            maximum = int(raw_input('Maximum: '))
            break

        except ValueError:
            print 'Not allowed! Use an Integer as Input!'
