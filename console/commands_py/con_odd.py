import argparse
from 
tmp = ''

parser = argparse.ArgumentParser(prog="odd",description='Tests if the given number is odd.',add_help=True)
parser.add_argument('number_to_be_tested', type=int, metavar='number', help='The number to be tested.')
#parser.set_defaults(func=help)
args = parser.parse_args()
