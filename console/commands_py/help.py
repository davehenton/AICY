import argparse
tmp = ''

parser = argparse.ArgumentParser(prog="help",description='Prints the help.',add_help=True)
parser.add_argument('-c', '--command', default=argparse.SUPPRESS, choices=['gcd'], help='shows the help for a specific command')
parser.set_defaults(func=help)

parser.parse_args()
