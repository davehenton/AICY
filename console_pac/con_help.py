def help_con(argument_list):

import argparse
tmp = ''

parser = argparse.ArgumentParser(prog="help",description='Prints the help.',add_help=True)
parser.add_argument('-c', '--command', choices=['gcd','odd'], help='shows the help for a specific command')
#parser.set_defaults(func=help)
args = parser.parse_args()

if args.command is None:
    print()
    print('     Thank you for using the     TEXT-CODING-LIBARY      :')
    print(
    '''
        If you want more detailed information
        about a specified command, type:
            'help -c [specified command]

        Possible [specified command]s are:
            - 'gcd'
            - 'odd'

        For the usage of this command, type:
            'help -h' or 'help --help'
    ''')

if args.command == 'gcd':
    print(
    '''
        The 'gcd' command founds you the
            greatest common divisor of two
            numbers.

        USAGE:
            gcd [int1] [int2]
    '''
    )

if args.command == 'odd':
    print(
    '''
        The 'odd' command tests if a
            number is odd.

        USAGE:
            odd [int]
    '''
    )
