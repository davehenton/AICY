import argparse
from text_coding_lib.math_lib.basic_math_lib.divisor_module import isOdd
tmp = ''

parser = argparse.ArgumentParser(prog="odd",description='Tests if the given number is odd.',add_help=True)
parser.add_argument('number_to_be_tested', type=int, metavar='number', help='The number to be tested.')
#parser.set_defaults(func=help)
args = parser.parse_args()

a = isOdd(number_to_be_tested)
print(a)
